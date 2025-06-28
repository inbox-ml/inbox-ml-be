from fastapi import APIRouter
from pydantic import BaseModel
from services.agent_service import AgentService
from services.image_service import ImageService
from decorators.require_user import require_user

router = APIRouter(prefix="/agent", tags=["Agent"])

class FileItem(BaseModel):
    fileBlob: str

@router.post("/summurize")
async def handleAsk(file_item: FileItem):
    img = ImageService(file_item.fileBlob)
    img_content = img.get_content_from_image()
    agent = AgentService("Summirize content from the mail. Response should be no more then 10 sentances.")
    agent_response = await agent.ask_agent(f"Mail content: {img_content}")
    return agent_response
