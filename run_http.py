import asyncio, os
from agents.mcp import MCPServerStreamableHttp
from dotenv import load_dotenv
from runner import run_with_server

load_dotenv()

def http_server():
    return MCPServerStreamableHttp(
        name="Vincent MCP Server (http)",
        params={"url": os.getenv("MCP_HTTP_SERVER_URL")},
    )

if __name__ == "__main__":
    asyncio.run(run_with_server(http_server))
