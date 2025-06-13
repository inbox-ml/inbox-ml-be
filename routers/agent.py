from fastapi import APIRouter
from services.agent_service import AgentService
from services.image_service import ImageService

router = APIRouter(prefix="/agent", tags=["Agent"])

@router.post("/summurize")
async def handleAsk():
    
    img = ImageService()
    img_content = img.get_content_from_image()
    agent = AgentService("Summirize content from the mail. Response should be no more then 10 sentances.")
    agent_response = await agent.ask_agent(f"Mail content: {img_content}")
    return agent_response
