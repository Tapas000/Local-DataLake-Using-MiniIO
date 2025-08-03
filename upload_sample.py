import boto3
import os

# MinIO credentials
endpoint = "http://localhost:9000"
access_key = "admin"
secret_key = "password123"
bucket_name = "my-datalake"

# Connect to MinIO
s3 = boto3.client(
    "s3",
    endpoint_url=endpoint,
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
)

# Upload all files from sample_data/
for file_name in os.listdir("sample_data"):
    file_path = os.path.join("sample_data", file_name)
    print(f"Uploading {file_path}")
    s3.upload_file(file_path,"my-datalake", file_name)
