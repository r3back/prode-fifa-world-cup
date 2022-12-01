from abc import abstractmethod


class UserRepository:
    @abstractmethod
    def get_user_by_email_and_password(self, email, password):
        pass

    @abstractmethod
    def save_user(self, user):
        pass

    @abstractmethod
    def get_user_by_email(self, email):
        pass

    @abstractmethod
    def add_new_user(self, user):
        pass

    @abstractmethod
    def get_all_users(self):
        pass
