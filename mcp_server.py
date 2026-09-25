import boto3
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("AI DevOps MCP")


@mcp.tool()
def aws_identity() -> dict:
    """
    Return the current AWS account identity.
    """
    sts = boto3.client("sts")

    response = sts.get_caller_identity()

    return {
        "Account": response["Account"],
        "Arn": response["Arn"]
    }


if __name__ == "__main__":
    mcp.run()
