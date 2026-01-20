from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel

mcp = FastMCP(name="calculator-server", sse_path="/mcp", message_path="/mcp/messages", stateless_http=True)

class AddInput(BaseModel):
    a: float
    b: float

@mcp.tool()
def add(a: float, b: float) -> dict:
    result = a + b
    return {
        "content": [{"type": "text", "text": f"{a} + {b} = {result}"}],
        "structuredContent": {"a": a, "b": b, "result": result},
        "_meta": {
            "openai/outputTemplate": "ui://widget/calculator-result.html",
            "openai/resultCanProduceWidget": True
        }
    }  