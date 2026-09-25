def create_plan(task):
    if "s3" in task.lower() and "website" in task.lower():
        return [
            "Create S3 bucket",
            "Enable static website hosting",
            "Upload index.html",
            "Test S3 website configuration"
        ]

    return ["Task not supported yet"]
