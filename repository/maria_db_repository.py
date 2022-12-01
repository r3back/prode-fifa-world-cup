import json
from collections.abc import Sequence

from game.user_prode import UserProde
from repository.abstract_repository import UserRepository
import mariadb

from game.user import User


class MariaDBUserRepository(UserRepository):
    def __init__(self, config):
        self.connection = mariadb.connect(
            user=config.user_name,
            password=config.password,
            host=config.host,
            port=config.port,
            database=config.database,
            autocommit=True
        )
        self.create_table()

    def create_table(self):
        sql_statement = "CREATE TABLE IF NOT EXISTS Users (UserId int AUTO_INCREMENT, Name varchar(255), Email varchar(" \
              "255), Password varchar(255), Data varchar(29999), PRIMARY KEY (UserId));"
        self.execute_statement(sql_statement)

    def get_user_by_email_and_password(self, email, password):
        sql_statement = "SELECT Name, Email, Password, Data FROM `Users` WHERE Email=? AND Password=?"

        sql_return = self.execute_and_get_statement(sql_statement, (email, password))

        user = None if len(sql_return) == 0 else self.deserialize(sql_return)

        return user

    def add_new_user(self, user):
        sql_statement = "INSERT INTO `Users` (`Name`, `Email`, `Password`, `Data`) VALUES (%s, %s, %s, %s)"

        # Changes prodes to json to save in db as string
        user_prodes = user.get_serialized_prodes()

        self.execute_statement(sql_statement, (user.name, user.email, user.password, user_prodes))

    def save_user(self, user):
        sql_statement = "UPDATE `Users` SET Name=?, Email=?, Password=?, Data=? WHERE Email=?"

        # Changes prodes to json to save in db as string
        user_prodes = user.get_serialized_prodes()

        self.execute_statement(sql_statement, (user.name, user.email, user.password, str(user_prodes), user.email))

    def get_user_by_email(self, email):
        sql_statement = "SELECT * FROM `Users` WHERE Email=?"

        sql_return = self.execute_and_get_statement(sql_statement, [email])

        return None if len(sql_return) == 0 else User(sql_return[0], sql_return[1], sql_return[2], [])

    def get_by_id(self, user_id):
        sql_statement = "SELECT Name, Email, Password, Data FROM `Users` WHERE UserId=?"

        sql_return = self.execute_and_get_statement(sql_statement, user_id)

        return None if len(sql_return) == 0 else self.deserialize(sql_return)

    def get_all_users(self):
        ids = self.get_all_user_ids()

        users = list(map(lambda user_id: self.get_by_id(user_id), ids))

        return list(filter(lambda user: user is not None, users))

    def get_all_user_ids(self):
        sql = "SELECT UserId FROM `Users`"

        sql_return = self.execute_and_get_statement(sql)

        return None if len(sql_return) == 0 else map(lambda dato: str(dato), sql_return)

    def execute_statement(self, statement, data: Sequence = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(statement, data)

    def execute_and_get_statement(self, statement, data: Sequence = ()):
        iterable = []
        with self.connection.cursor() as cursor:
            cursor.execute(statement, data)
            for valor in cursor:
                return valor
            return iterable

    @staticmethod
    def deserialize(sql_return):
        prodes_json = json.loads(sql_return[3])

        prodes_deserialized = list(
            map(lambda dato: UserProde(dato["equipo_local"], dato["equipo_visitante"], dato["equipo_local_goles"],
                                       dato["equipo_visitante_goles"], dato["email_enviado"], dato["goles_reales_local"],
                                       dato["goles_reales_visitante"]), prodes_json))

        return User(sql_return[0], sql_return[1], sql_return[2], prodes_deserialized)
