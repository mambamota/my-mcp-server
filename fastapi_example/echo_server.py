from mcp.server.fastmcp import FastMCP

mcp = FastMCP(name="EchoServer", stateless_http=True)


@mcp.tool(description="A simple echo tool")
def echo(message: str) -> str:
    return f"Echo: {message}"

@mcp.tool(description="Test tool that returns a secret word")
def secret_phrase() -> str:
    return "the secret word is 'eureka'"
