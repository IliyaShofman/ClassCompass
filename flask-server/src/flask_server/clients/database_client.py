import firebase_admin
from firebase_admin import credentials, firestore

class DataBaseClient:
    """DataBaseClient class"""

    def __init__(self, auth_path, testing=False):
        # Authenticate credentials so we can access our firebase project
        cred = credentials.Certificate(auth_path)
        firebase_admin.initialize_app(cred)

        # Initialize Firestore db
        self._db = firestore.client()
        self._testing = testing

    @property
    def user_profiles_collection(self):
        if self._testing:
            return self._db.collection("TestUserProfiles")
        else:
            return self._db.collection("UserProfiles")
