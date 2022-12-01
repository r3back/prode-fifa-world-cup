from loader.database_loader import ConfigLoader
from repository.abstract_repository import UserRepository
from repository.maria_db_repository import MariaDBUserRepository
from repository.memory_repository import InMemoryRepository
from repository.mysql_repository import MySQLUserRepository


class DatabaseFactory:
    __instance = None

    def __init__(self):
        self.config = ConfigLoader.get_database_config()

    @staticmethod
    def get_instance():
        if DatabaseFactory.__instance is None:
            DatabaseFactory.__instance = DatabaseFactory()
        return DatabaseFactory.__instance

    def create_database(self) -> UserRepository:
        if self.config.db_type == "MARIADB":
            return MariaDBUserRepository(self.config)
        elif self.config.db_type == "MYSQL":
            return MySQLUserRepository(self.config)
        elif self.config.db_type == "FLAT":
            return InMemoryRepository()
        else:
            return InMemoryRepository()
