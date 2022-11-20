import os
import pathlib

import yaml

from me.reb4ck.prode.config.DatabaseConfig import DatabaseConfig


class ConfigLoader:
    @staticmethod
    def get_database_config():

        path = str(pathlib.Path(__file__).parent.resolve()) + '/../../../../resources'

        os.chdir(path)

        config = yaml.safe_load(open("config.yml"))

        host = config.get("host")
        database = config.get("database")
        user_name = config.get("user_name")
        password = config.get("password")
        port = config.get("port")
        use_ssl = config.get("use_ssl")
        db_type = config.get("db_type")

        return DatabaseConfig(host, database, user_name, password, port, use_ssl, db_type)

