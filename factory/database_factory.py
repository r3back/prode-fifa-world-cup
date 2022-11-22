from loader.database_loader import ConfigLoader
from repository.maria_db_repository import MariaDBUserRepository


class DatabaseFactory():

    def __init__(self):
        self.config = ConfigLoader().get_database_config()

    def obtener_base_de_datos(self):
        if self.config.db_type == "MARIADB":
            return MariaDBUserRepository(self.config)
        elif self.config.db_type == "MYSQL":
            return None
        else:
            return None



