# import pymysql
# from DBUtils.SteadyDB import connect
from abc import abstractmethod


# db = connect(
#  creator = pymysql,
#  user = 'guest', password = '', database = 'name',
#  autocommit = True, charset = 'utf8mb4',
#  cursorclass = pymysql.cursors.DictCursor)

# def iniciar_conexion():
class UserRepository():
    @abstractmethod
    def obtener_por_email_y_contraseña(self, email, password):
        pass

    @abstractmethod
    def guardar_usuario(self, usuario):
        pass
