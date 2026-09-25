import boto3
import uuid

REGION = "us-east-1"


def create_s3_bucket():
    s3 = boto3.client("s3", region_name=REGION)

    bucket_name = f"ai-devops-lab-{uuid.uuid4().hex[:8]}"

    s3.create_bucket(Bucket=bucket_name)

    print(f"AWS Agent: Created bucket: {bucket_name}")

    return bucket_name


def enable_website(bucket_name):
    s3 = boto3.client("s3", region_name=REGION)

    s3.put_bucket_website(
        Bucket=bucket_name,
        WebsiteConfiguration={
            "IndexDocument": {
                "Suffix": "index.html"
            }
        }
    )

    print("AWS Agent: Static website hosting enabled")


def upload_index(bucket_name):
    s3 = boto3.client("s3", region_name=REGION)

    html = """
    <html>
        <body>
            <h1>Hello from AI DevOps Assistant</h1>
        </body>
    </html>
    """

    s3.put_object(
        Bucket=bucket_name,
        Key="index.html",
        Body=html,
        ContentType="text/html"
    )

    print("AWS Agent: index.html uploaded")
