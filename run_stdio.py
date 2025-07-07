import asyncio, os, shutil
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
from runner import run_with_server

load_dotenv()

def stdio_server():
    return MCPServerStdio(
        name="Vincent MCP Server (stdio)",
        params={
            "command": "npx",
            "args": ["-y", "node", os.getenv("MCP_STDIO_SERVER_PATH")],
            "env": {
                "VINCENT_DELEGATEE_PRIVATE_KEY": os.getenv("VINCENT_DELEGATEE_PRIVATE_KEY"),
                "VINCENT_APP_JSON_DEFINITION": os.getenv("VINCENT_APP_JSON_DEFINITION"),
                # Or pass the Vincent App Id if not overriding anything
                # "VINCENT_APP_ID": os.getenv("VINCENT_APP_ID"),
            },
        },
    )

if __name__ == "__main__":
    if not shutil.which("npx"):
        raise RuntimeError("npx is not installed.  `sudo npm i -g npx`")
    asyncio.run(run_with_server(stdio_server))
