from agents import Agent, Runner, gen_trace_id, trace
from agents.mcp import MCPServer        # just for typing

async def _run_flow(mcp_server: MCPServer) -> None:
    """
    Build the agents once and execute the workflow against the
    given MCP server (stdio *or* http).
    """
    assistant = Agent(
        name="Vincent assistant",
        instructions="Use the Vincent MCP tools to do what is asked.",
        mcp_servers=[mcp_server],
    )

    coordinator = Agent(
        name="Coordinator",
        instructions="Make a plan and use your assistants to complete it.",
        handoffs=[assistant],
    )

    message = (
        "Check who my delegators are and then check the native balance "
        "in base blockchain of the first one."
    )
    print(f"Running: {message}")

    result = await Runner.run(starting_agent=coordinator, input=message)
    print(result.final_output)


async def run_with_server(server_factory):
    """
    Helper that wraps 'async with server_factory() as server' so the
    callers only pass the ctor or lambda that returns the right server.
    """
    async with server_factory() as server:
        trace_id = gen_trace_id()
        with trace(workflow_name="Vincent MCP Example", trace_id=trace_id):
            print(
                f"View trace: https://platform.openai.com/traces/trace?"
                f"trace_id={trace_id}\n"
            )
            await _run_flow(server)
