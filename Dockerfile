FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y curl unzip ca-certificates && \
    curl -o /tmp/terraform.zip \
    https://releases.hashicorp.com/terraform/1.16.4/terraform_1.16.4_linux_amd64.zip && \
    unzip /tmp/terraform.zip -d /usr/local/bin && \
    rm /tmp/terraform.zip && \
    rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir boto3

CMD ["python", "app.py"]
