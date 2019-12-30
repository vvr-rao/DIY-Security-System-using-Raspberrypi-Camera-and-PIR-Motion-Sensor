# Raspberry-pi-Camera-Take-picture-and-save-to-S3
Quick piece of code I wrote to take a picture using my Raspberry Pi Camera Module and upload to AWS S3

Hardware needed;
1) Raspberry Pi 4
2) Camera Module

Software;
1) An AWS account (I created a private bucket)
2) Python (2.7,3.5,3.7) shoudl all work. This should already be on the Pi. If not download it. Then download Boto3. I did not download AWS CLI.

Other;
1) Connection to internet

The code handles still images. Video capture and upload should be posible. Planning to integrate with some sort or motion sensor.
