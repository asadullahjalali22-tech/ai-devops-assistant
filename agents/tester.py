import boto3
from botocore.exceptions import ClientError

REGION = "us-east-1"


def test_s3_bucket(bucket_name):
    s3 = boto3.client("s3", region_name=REGION)

    print("\n--- TESTER AGENT ---")

    try:
        s3.head_bucket(Bucket=bucket_name)
        print("Bucket exists: OK")
    except ClientError:
        print("Bucket exists: FAILED")
