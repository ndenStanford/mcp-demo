import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStdio

async def main():  
    server = MCPServerStdio(  
            'uvx', args=["mcp-server-time"], timeout=10
    )

    agent = Agent(  
        'openai:gpt-4o-mini'
    )
    agent = Agent('openai:gpt-4o-mini', toolsets=[server])
    result = await agent.run("What's the current time in New York and Tokyo?. Call the mcp server.")

    print(result)

if __name__ == "__main__":
    asyncio.run(main())
   