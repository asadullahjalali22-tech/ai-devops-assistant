import asyncio
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command=sys.executable,
        args=["mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()

            print("\n--- MCP TOOLS ---")
            for tool in tools.tools:
                print(tool.name)

            result = await session.call_tool(
                "aws_identity",
                arguments={}
            )

            print("\n--- AWS IDENTITY ---")
            for item in result.content:
                if hasattr(item, "text"):
                    print(item.text)


if __name__ == "__main__":
    asyncio.run(main())
