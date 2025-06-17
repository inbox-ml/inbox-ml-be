import os
import firebase_admin
from firebase_admin import firestore, credentials, App
from google.cloud.firestore import Client

class FirebaseService:

    __app: App
    __db: Client

    @staticmethod
    def init():
        current_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.abspath(os.path.join(current_path, ".."))
        cred = credentials.Certificate(os.path.join(root_path, "firebase-service-account.json"))
        print(cred.project_id)
        FirebaseService.__app = firebase_admin.initialize_app(cred)
        FirebaseService.__db = firestore.client(app=FirebaseService.__app, database_id="oh-snap-prod")

    @staticmethod
    def get_db() -> Client:
        return   FirebaseService.__db  