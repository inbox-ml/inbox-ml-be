from fastapi import APIRouter
from services.agent_service import OhSnapAgent
from services.image_service import IhSnapImage

router = APIRouter(prefix="/agent", tags=["Agent"])

@router.post("/ask")
async def handleAsk():
    
    img = IhSnapImage()
    img_content = img.get_content_from_image()
    agent = OhSnapAgent("Summirize content from the mail. Response should be no more then 10 sentances.")
    agent_response = await agent.ask_agent(f"Mail content: {img_content}")
    return agent_response
