from dto.user_dto import UserCreate, UserUpdate, User
from services.firebase_service import FirebaseService


class UserSerivice:

    __COLLECTION_NAME = "users"
    __HISTORY_COLLECTION_NAME = "history"

    @staticmethod
    def create(user: UserCreate):
        db = FirebaseService.get_db()
        res = db.collection(UserSerivice.__COLLECTION_NAME).add(user.model_dump(), user.email)
        return res

    @staticmethod
    def update(doc_id: str, data: UserUpdate):
        db = FirebaseService.get_db()
        res = db.collection(UserSerivice.__COLLECTION_NAME).document(doc_id).update(data)
        return res

    @staticmethod
    def get(doc_id: str) -> User:
        db = FirebaseService.get_db()
        res = db.collection(UserSerivice.__COLLECTION_NAME).document(doc_id).get()
        return res.to_dict()
    
    @staticmethod
    def get_history(doc_id: str) -> User:
        print(doc_id)
        db = FirebaseService.get_db()
        docs = db.collection(UserSerivice.__COLLECTION_NAME).document(doc_id).collection(UserSerivice.__HISTORY_COLLECTION_NAME).get()
        for i in range(len(docs)):
            data = docs[i].to_dict()
            data["id"] = docs[i].id
            docs[i] = data
        return docs