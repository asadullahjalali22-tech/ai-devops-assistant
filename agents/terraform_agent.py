import subprocess
import uuid
from pathlib import Path

TERRAFORM_DIR = Path(__file__).resolve().parent.parent / "terraform"


def generate_terraform():
    bucket_name = f"ai-devops-tf-{uuid.uuid4().hex[:8]}"

    terraform_code = f"""
terraform {{
  required_providers {{
    aws = {{
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }}
  }}
}}

provider "aws" {{
  region = "us-east-1"
}}

resource "aws_s3_bucket" "devops_bucket" {{
  bucket = "{bucket_name}"
}}

output "bucket_name" {{
  value = aws_s3_bucket.devops_bucket.bucket
}}
"""

    main_tf = TERRAFORM_DIR / "main.tf"
    main_tf.write_text(terraform_code)

    print(f"Terraform Agent: Generated infrastructure for {bucket_name}")

    return bucket_name


def terraform_init():
    print("\n--- TERRAFORM INIT ---")

    return subprocess.run(
        ["terraform", "init"],
        cwd=TERRAFORM_DIR
    ).returncode


def terraform_plan():
    print("\n--- TERRAFORM PLAN ---")

    return subprocess.run(
        ["terraform", "plan"],
        cwd=TERRAFORM_DIR
    ).returncode


def terraform_apply():
    print("\n--- TERRAFORM APPLY ---")

    return subprocess.run(
        ["terraform", "apply", "-auto-approve"],
        cwd=TERRAFORM_DIR
    ).returncode
