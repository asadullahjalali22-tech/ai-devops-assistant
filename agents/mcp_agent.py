import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def get_aws_identity():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            result = await session.call_tool(
                "aws_identity",
                arguments={}
            )

            for item in result.content:
                if hasattr(item, "text"):
                    return item.text

    return None


def aws_identity():
    return asyncio.run(get_aws_identity())
