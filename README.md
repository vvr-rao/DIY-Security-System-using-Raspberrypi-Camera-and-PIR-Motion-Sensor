# DIY Security System. Uses Raspberry Pi Camera and Motion Sensor modules to detect motion, capture pictures and upload to AWS S3
Quick piece of code I wrote to take a picture using my Raspberry Pi Camera Module and upload to AWS S3. Putting the file in AWS opens up the power of AWS to access and process the images (e.g. facial recognition via AWS Rekognition or Sagemaker). For now, I also built in a quick email alert when an object is added to my bucket using an S3 Trigger on the bucket and Lambda

Hardware used;
1) Raspberry Pi 4 B Quad Core 64 (4GB)
2) Camera Module V2
3) HC-SR501 PIR (Passive Infra Red) Motion Sensor

Software;
1) An AWS account 
        I created a private bucket to store files
        A Lambda, SES to send emails - FYI: used existing Blueprint s3-get-object-python
2) Python (2.7,3.5,3.7) should all work. This should already be on the Pi. If not download it. Then download and install Boto3. I did NOT install AWS CLI.

Other;
1) Connection to internet

The code handles still images. Video capture and upload should be posible. 
