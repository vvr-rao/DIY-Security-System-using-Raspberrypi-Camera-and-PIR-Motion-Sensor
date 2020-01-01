# DIY Security System. Uses Raspberry Pi Camera and Motion Sensor modules to detect motion, capture pictures and upload to AWS S3
Quick piece of code I wrote to take a picture using my Raspberry Pi Camera Module and upload to AWS S3

Hardware used;
1) Raspberry Pi 4 B Quad Core 64 (4GB)
2) Camera Module V2
3) HC-SR501 PIR (Passive Infra Red) Motion Sensor

Software;
1) An AWS account (I created a private bucket)
2) Python (2.7,3.5,3.7) should all work. This should already be on the Pi. If not download it. Then download and install Boto3. I did NOT install AWS CLI.

Other;
1) Connection to internet

The code handles still images. Video capture and upload should be posible. 
