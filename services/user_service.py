from dto.user_dto import UserCreate
from services.firebase_service import FirebaseService


class UserSerivice:

    __COLLECTION_NAME = "users"

    @staticmethod
    def create(user: UserCreate):
        db = FirebaseService.get_db()
        res = db.collection(UserSerivice.__COLLECTION_NAME).add(user.model_dump(), user.email)
        return res

    @staticmethod
    def update(doc_id: str, data: dict):
        db = FirebaseService.get_db()
        res = db.collection(UserSerivice.__COLLECTION_NAME).document(doc_id).update(data)
        return res

    @staticmethod
    def get(doc_id: str):
        db = FirebaseService.get_db()
        res = db.collection(UserSerivice.__COLLECTION_NAME).document(doc_id).get()
        return res.to_dict()