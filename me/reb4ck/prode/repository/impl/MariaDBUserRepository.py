import json
from collections.abc import Sequence

from me.reb4ck.prode.repository.UserRepository import UserRepository
import mariadb

from me.reb4ck.prode.user.User import User


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
        self.crear_tabla()

    def crear_tabla(self):
        sql = "CREATE TABLE IF NOT EXISTS Users (UserId int AUTO_INCREMENT, Name varchar(255), Email varchar(" \
              "255), Password varchar(255), Data varchar(29999), PRIMARY KEY (UserId));"
        self.execute(sql)

    def obtener_por_email_y_contraseña(self, email, password):
        sql = "SELECT Name, Email, Password, Data FROM `Users` WHERE Email=? AND Password=?"

        retorno = self.executeGet(sql, (email, password))

        if len(retorno) == 0:
            return None
        else:
            return User(retorno[0], retorno[1], retorno[2], retorno[3])

    def guardar_usuario(self, usuario):
        sql = "INSERT INTO `Users` (`Name`, `Email`, `Password`, `Data`) VALUES (%s, %s, %s, %s)"

        datos = str(usuario.datos)

        self.execute(sql, (usuario.nombre, usuario.email, usuario.contrasena, datos))

    def obtener_por_email(self, email):
        sql = "SELECT Name, Email, Password, Data FROM `Users` WHERE Email=?"

        retorno = self.executeGet(sql, [email])

        if len(retorno) == 0:
            return None
        else:
            #datos = json.load(retorno[3])
            return User(retorno[0], retorno[1], retorno[2], [])

    def execute(self, statement, data: Sequence = ()):
        with self.connection.cursor() as cursor:
            cursor.execute(statement, data)

    def executeGet(self, statement, data: Sequence = ()):
        iterable = []
        with self.connection.cursor() as cursor:
            cursor.execute(statement, data)
            for valor in cursor:
                return valor
            return iterable
