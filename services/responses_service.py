import os
import base64
from io import BytesIO
from openai import OpenAI
from google.cloud import storage
from datetime import timedelta


class OhSnapResponse:

    _client: OpenAI

    def __init__(self):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebase-service-account.json"
        self._client = OpenAI()

    def get_image(self):
        client = storage.Client()
        bucket = client.bucket("oh-snap-bcacf.firebasestorage.app")
        blob = bucket.blob("test.jpeg")
        return blob.generate_signed_url(expiration=timedelta(minutes=15))  

    def create_vector_store(self):
        vector_store = self._client.vector_stores.create(
            name="knowledge_base"
        )
        return vector_store.id
    

    def prepare_file_for_assistant(self, file: str):
        file_obj = BytesIO(base64.b64decode(file.split(",")[1]))
        file_obj.name = "test.jpeg"
        result = self._client.files.create(
                file=file_obj,
                purpose="vision"
        )
        return result.id
            


    def get_response(self, file: str):
        print(file)
        file_id = self.prepare_file_for_assistant(file=file)
        response = self._client.responses.create(
            model="gpt-4.1-mini-2025-04-14",
            input=[{
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "Get text from the image"},
                    {"type": "input_image","file_id": file_id},
                ]
            }]
        ) 
        #make sure to delete files 
        self._client.files.delete(file_id)
        
        return response.output_text     

