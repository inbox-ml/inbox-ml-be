from dto.user_dto import UserCreate
from services.firebase_service import FirebaseService


class UserSerivice:

    @staticmethod
    def create(user: UserCreate):
        db = FirebaseService.get_db()
        print (user)
        res = db.collection("users").add(user.model_dump(), user.email)
        print (res)
        return res

    @staticmethod
    def update():
        pass

    @staticmethod
    def get():
        pass