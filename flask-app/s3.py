import boto3
import os
from botocore.client import ClientError

# load environment variable
from dotenv import load_dotenv

load_dotenv()

# our very secret buckets
bucket = os.environ.get("BUCKET_NAME", "default")
region = os.environ.get("REGION", "eu-west-2")
print(f"bucket name is {bucket}")


# use s3 bucket as resource
s3 = boto3.resource("s3")
client = s3.meta.client
try:
    result = client.head_bucket(Bucket=bucket)
    print(result)
except ClientError:
    # The bucket does not exist or you have no access.
    print(f"bucket {bucket} not found")
    # create a bucket if not exist
    s3.create_bucket(
        Bucket=bucket, CreateBucketConfiguration={"LocationConstraint": region}
    )
    
except client.exceptions.BucketAlreadyExists:
    print(f"sorry the bucket {bucket} already exists in {region}")


# list all our buckets
def list_all_buckets(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)
