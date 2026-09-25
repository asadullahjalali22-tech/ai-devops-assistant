
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 6.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "devops_bucket" {
  bucket = "ai-devops-tf-54daefc1"
}

output "bucket_name" {
  value = aws_s3_bucket.devops_bucket.bucket
}
