import base64
from services.responses_service import OhSnapResponse


class ImageService:

    __image_base64: bytes

    def __init__(self, image_base64: bytes = None):
        self.__image_base64 = image_base64

    def save_to_the_bucket(self, bucket: str, name: str):
        pass

    def get_from_the_bucket(self, bucket: str, file_id: str):
        pass

    def get_content_from_image(self) -> str:
           r = OhSnapResponse()
           return r.get_response()