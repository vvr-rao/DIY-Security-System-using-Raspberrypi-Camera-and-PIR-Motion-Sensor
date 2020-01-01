from picamera import PiCamera
from time import sleep
from datetime import datetime
import boto3
import RPi.GPIO as GPIO
import os
import curses


GPIO.setmode(GPIO.BOARD)
pir = 8
GPIO.setup(pir, GPIO.IN)
sleep(2)
ACCESS_KEY = '<YOUR_ACCESS_KEY>'
SECRET_KEY = '<YOUR_SECRET_ACCESS_KEY>'

#take the picture. Max resolution. should give a 3 MiB file
camera = PiCamera()

#camera.rotation = 270
camera.resolution = (2592, 1944)
camera.framerate = 15

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(3)

screen.keypad(True)

print(datetime.now())

def capturepic():
    curtime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    camera.annotate_text = curtime
    camera.annotate_text_size = 160
    camera.start_preview()
    sleep(2)
    savefile = '/home/pi/camerapics/' + curtime + '.jpg'
    camera.capture(savefile)
    camera.stop_preview()
    #upload to AWS S3
    client = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    client.upload_file(savefile,'BUCKET_NAME',curtime+'.jpg')
    print('Done')
    return;

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            print('Exit')
            break
        else:
            if GPIO.input(pir) == True:
                print('Motion detected')
                capturepic()
                

finally:
    GPIO.cleanup()
    camera.close()
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()