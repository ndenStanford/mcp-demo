import asyncio
import os
from langchain_openai import ChatOpenAI
from mcp_use import MCPAgent, MCPClient

async def main():
    # Create MCPClient from configuration dictionary

    client = MCPClient.from_config_file(
        os.path.join(".vscode/mcp_use_mcp.json")
    )
    print(client)

    # # # Create LLM
    # llm = ChatOpenAI(model="gpt-4o-mini")

    # # Create agent with the client
    # agent = MCPAgent(llm=llm, client=client, max_steps=30)

    # # Run the query
    # result = await agent.run(
    #     "What's the current time in New York and Tokyo?",
    #     # "What's the new AI trend?",
    # )
    # print(f"\nResult: {result}")

if __name__ == "__main__":
    asyncio.run(main())
    # main()

# # def main():
# #     print("Hello from mcp!")
    
# #     roulette_agent = Agent(  
# #         'openai:gpt-4o-mini',
# #         deps_type=int,
# #         output_type=bool,
# #         system_prompt=(
# #             'Use the `roulette_wheel` function to see if the '
# #             'customer has won based on the number they provide.'
# #         ),
# #     )


# # if __name__ == "__main__":
# #     main()