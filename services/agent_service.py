from agents import Agent, Runner, WebSearchTool, RunContextWrapper, GuardrailFunctionOutput, input_guardrail
from services.firebase_service import FirebaseService
from pydantic import BaseModel

class MailOutput(BaseModel):
    reasoning: str
    is_not_valid_request: bool

class ContentSummaryOutput(BaseModel):
    is_scam: bool
    category: str
    summary_title: str
    summary: str        


class AgentService:

    __agent: Agent
    __static_input_guardrail_agent: Agent = Agent(
            name="Content Validator", 
            instructions="Check if content is a mail or email", 
            model="gpt-4.1-nano-2025-04-14",
            output_type=MailOutput
            )

    def __init__(self, instructions: str):
        self.__agent = Agent(
            name="Inbox Checker", 
            instructions=instructions, 
            model="gpt-4.1-mini-2025-04-14",
            tools=[WebSearchTool()],
            output_type=ContentSummaryOutput
            )

    async def ask_agent(self, prompt: str, email: str):
        self.__agent.input_guardrails=[self.request_guardrail]
        result = await Runner.run(self.__agent, prompt)
        await self.save_response(data=result.final_output, email=email)
        return result.final_output

    @staticmethod
    @input_guardrail
    async def request_guardrail(ctx: RunContextWrapper, agent: Agent, input: str) -> GuardrailFunctionOutput:
        result = await Runner.run(AgentService.__static_input_guardrail_agent, input, context=ctx.context)
        return GuardrailFunctionOutput(tripwire_triggered=result.final_output.is_not_valid_request, output_info=result.final_output)
    

    async def save_response(self, data, email: str):
        db = FirebaseService.get_db()
        print(email)
        print(data)
        db.collection("users").document(email).collection("history").add(document_data=data.dict())