import json
import urllib.parse
import boto3
from datetime import datetime

print('Loading function')

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    try:
        curtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])
        #Insert Send Email Code between these two lines
        client = boto3.client('ses')
        
        subject = 'Motion detected on security system'
        body = """
            <b>Alert</b><br>
            Motion has been detected on you security system. Please log in to your AWS Account to view.
        """ + curtime
        message = {"Subject": {"Data": subject}, "Body": {"Html": {"Data": body}}}
        mailresponse = client.send_email(Source="<source email address>", Destination = {"ToAddresses": ["<destination email address>"]}, Message = message)
        #Insert Send Email Code between these two lines
        #return response['ContentType']
        return mailresponse['MessageId']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e
