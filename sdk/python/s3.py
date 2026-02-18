import os
import boto3
import bs4
import uuid
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

### upload files to bucket
prefix = "uuid"
for i in range(5):
    filename = f"testfile_{i}.txt"
    with open(f"testfiles/{filename}","w") as f:
        f.write(str(uuid.uuid4()))
        print(f"writing file {filename}")
    with open(f"testfiles/{filename}","rb") as f:
        s3.upload_fileobj(f, bucket_name, f"{prefix}/{filename}")
        # s3.put_object(bucket_name,Key,Body) #For small files.
        print(f"uploading file {filename} to s3/{bucket_name}/{prefix}/{filename}")

#download files
# s3.download_file(bucket_name, file_key, "example.txt")


