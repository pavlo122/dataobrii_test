import json
import boto3

def lambda_handler(event, context):
    client = boto3.client('s3')
    response = client.list_objects(
        Bucket='your_bucket_here'
    )
    for records in response['Contents']:
        print(records['Key'])
