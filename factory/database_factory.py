from me.reb4ck.prode.config.DBConfigLoader import ConfigLoader
from me.reb4ck.prode.repository.impl.MariaDBUserRepository import MariaDBUserRepository


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



