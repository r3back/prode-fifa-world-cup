from factory.database_factory import DatabaseFactory
from repository.abstract_repository import UserRepository


class UserService:
    __instance = None

    @staticmethod
    def get_instance():
        if UserService.__instance is None:
            UserService.__instance = UserService()
        return UserService.__instance

    def __init__(self):
        self.repository: UserRepository = DatabaseFactory.get_instance().create_database()

    def get_user_by_email_and_password(self, email, password):
        return self.repository.get_user_by_email_and_password(email, password)

    def get_user_by_email(self, email):
        return self.repository.get_user_by_email(email)

    def save_user(self, usuario):
        return self.repository.save_user(usuario)

    def add_new_user(self, usuario):
        return self.repository.add_new_user(usuario)

    def get_all_users(self):
        return self.repository.get_all_users()
