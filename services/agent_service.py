from agents import Agent, Runner, WebSearchTool

class OhSnapAgent:

    __agent: Agent

    def __init__(self, instructions: str):
        self.__agent = Agent(
            name="test", 
            instructions=instructions, 
            model="gpt-4.1-mini-2025-04-14",
            tools=[WebSearchTool()]
            )

    async def ask_agent(self, prompt: str):
        result = await Runner.run(self.__agent, prompt)
        return result.final_output
