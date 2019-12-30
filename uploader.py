from picamera import PiCamera
from time import sleep
from datetime import datetime
import boto3

#take the picture. Max resolution. should give a 3 MiB file
camera = PiCamera()

#camera.rotation = 270
camera.resolution = (2592, 1944)
camera.framerate = 15
print(datetime.now())

curtime = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
camera.annotate_text = curtime
camera.annotate_text_size = 160
camera.start_preview()
sleep(2)
savefile = '/home/pi/camerapics/' + curtime + '.jpg'
#camera.capture('/home/pi/Desktop/image2.jpg')
camera.capture(savefile)
camera.stop_preview()

#upload to AWS S3
ACCESS_KEY = 'YOUR ACCESS KEY'
SECRET_KEY = 'YOUR SECRET ACCESS KEY'

client = boto3.client('s3',
                      aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

client.upload_file(savefile,'<INSERT_BUCKET_NAME>',curtime+'.jpg')

print('Done')