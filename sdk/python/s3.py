import os
import boto3
import bs4
from botocore.exceptions import ClientError

session = boto3.Session(profile_name="myprofile",region_name="us-east-1")
# bucket_name = os.environ["bucket_name"]
bucket_name = "my-example-py"

s3 = session.client("s3")
try:
    s3.create_bucket(
        Bucket="my-example-py"
    )
except ClientError as e:
    print("ERROR:", e.response["Error"]["Code"])

print(s3.list_objects(Bucket=bucket_name))