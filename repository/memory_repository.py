from repository.abstract_repository import UserRepository


class InMemoryRepository(UserRepository):
    users = None

    def __init__(self):
        self.users = []

    def get_user_by_email_and_password(self, email, password):
        return next(filter(lambda user: user.email == email and user.password == password, self.users), None)

    def add_new_user(self, user):
        pass

    def get_user_by_email(self, email):
        return next(filter(lambda user: user.email == email, self.users), None)

    def get_all_users(self):
        return self.users
