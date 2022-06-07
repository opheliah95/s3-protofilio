import boto3
import os
from botocore.client import ClientError

# load environment variable
from dotenv import load_dotenv
load_dotenv()

# our very secret buckets
bucket = os.environ.get("BUCKET_NAME", "default")
print(f"bucket name is {bucket}")



# use s3 bucket as resource
s3 = boto3.resource('s3')

try:
    s3.meta.client.head_bucket(Bucket=bucket.name)
except ClientError:
    # The bucket does not exist or you have no access.

 # list all our buckets
def list_all_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
