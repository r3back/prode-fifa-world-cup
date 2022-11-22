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
            return self.deserialize(retorno)

    def deserialize(self, retorno):
        datos = json.loads(retorno[3])

        prodes = []

        for dato in datos:
            prodes.append(UserProde(dato["equipo_local"], dato["equipo_visitante"], dato["equipo_local_goles"],
                                         dato["equipo_visitante_goles"], dato["email_enviado"], dato["goles_reales_local"], dato["goles_reales_visitante"]))

        return User(retorno[0], retorno[1], retorno[2], prodes)

    def agregar_usuario(self, usuario):
        sql = "INSERT INTO `Users` (`Name`, `Email`, `Password`, `Data`) VALUES (%s, %s, %s, %s)"

        self.datos = json.dumps(usuario.datos)

        self.execute(sql, (usuario.nombre, usuario.email, usuario.contrasena, self.datos))

    def guardar_usuario(self, usuario):
        sql = "UPDATE `Users` SET Name=?, Email=?, Password=?, Data=? WHERE Email=?"

        self.datos = usuario.get_serialized_datos()

        self.execute(sql, (usuario.nombre, usuario.email, usuario.contrasena, str(self.datos), usuario.email))

    def obtener_por_email(self, email):
        sql = "SELECT * FROM `Users` WHERE Email=?"

        retorno = self.executeGet(sql, [email])

        if len(retorno) == 0:
            return None
        else:
            # datos = json.load(retorno[3])
            return User(retorno[0], retorno[1], retorno[2], [])

    def obtener_por_id(self, id):
        sql = "SELECT Name, Email, Password, Data FROM `Users` WHERE UserId=?"

        retorno = self.executeGet(sql, (id))

        if len(retorno) == 0:
            return None
        else:
            return self.deserialize(retorno)

    def get_all_users(self):
        ids = self.get_all_ids()

        users = []

        for id in ids:
            user = self.obtener_por_id(id)
            if user is None:
                continue
            users.append(user)

        return users

    def get_all_ids(self):
        sql = "SELECT UserId FROM `Users`"

        retorno = self.executeGet(sql)

        ids = []

        if len(retorno) == 0:
            return None
        else:
            for dato in retorno:
                ids.append(str(dato))
            return ids

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
