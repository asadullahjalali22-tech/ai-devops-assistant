from agents.mcp_agent import aws_identity
from agents.planner import create_plan

from agents.terraform_agent import (
    generate_terraform,
    terraform_init,
    terraform_plan,
    terraform_apply
)

from agents.tester import test_s3_bucket

task = input("Enter your DevOps task: ")

plan = create_plan(task)

print("\n--- MCP AWS CHECK ---")
identity = aws_identity()
print(identity)

print("\n--- PLANNER AGENT ---")

for i, step in enumerate(plan, start=1):
    print(f"{i}. {step}")


if plan == ["Task not supported yet"]:
    print("\nTask not supported.")

else:
    approval = input("\nDo you approve this plan? (yes/no): ")

    if approval.lower() == "yes":
        print("\nApproved.")

        print("\n--- TERRAFORM AGENT ---")

        bucket = generate_terraform()

        if terraform_init() != 0:
            print("Terraform init failed.")
            exit()

        if terraform_plan() != 0:
            print("Terraform plan failed.")
            exit()

        apply_approval = input("\nApply Terraform plan? (yes/no): ")

        if apply_approval.lower() == "yes":
            if terraform_apply() == 0:
                print("\nTerraform deployment completed.")

                test_s3_bucket(bucket)

                print("\n--- RESULT ---")
                print(f"Bucket name: {bucket}")
                print("Workflow completed.")
            else:
                print("Terraform apply failed.")
        else:
            print("Terraform apply cancelled.")

    else:
        print("\nPlan not approved.")
