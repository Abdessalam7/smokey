"""Upload a local file to IBM COS (S3-compatible)."""
import boto3
from botocore.client import Config


def upload(local_path, bucket, object_key, endpoint, access_key, secret_key):
    s3 = boto3.client(
        "s3",
        endpoint_url=endpoint,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        config=Config(signature_version="s3v4"),
    )
    s3.upload_file(
        Filename=local_path,
        Bucket=bucket,
        Key=object_key,
        ExtraArgs={"ContentType": "application/json"},
    )
