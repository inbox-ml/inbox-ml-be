from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from services.agent_service import AgentService
from services.image_service import ImageService
from decorators.require_user import require_user

router = APIRouter(prefix="/agent", tags=["Agent"])

class FileItem(BaseModel):
    fileBlob: str

@router.post("/summurize")
@require_user
async def handleAsk(request: Request, file_item: FileItem):
    user = getattr(request.state, "user", None)
    if not user: 
        raise HTTPException(status_code=500, detail="Could not get user data")

    img = ImageService(file_item.fileBlob)
    img_content = img.get_content_from_image()
    agent = AgentService("Summirize content from the mail. Response should be no more then 10 sentances.")
    email = user.get("email")
    agent_response = await agent.ask_agent(f"Mail content: {img_content}", email)
    return agent_response
