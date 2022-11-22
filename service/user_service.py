from me.reb4ck.prode.factory.DatabaseFactory import DatabaseFactory


class UserService:
    __instance = None

    @staticmethod
    def get_instance():
        if UserService.__instance is None:
            UserService.__instance = UserService()
        return UserService.__instance

    def __init__(self):
        self.repository = DatabaseFactory().obtener_base_de_datos()

    def obtener_por_email_y_contraseña(self, email, contrasena):
        return self.repository.obtener_por_email_y_contraseña(email, contrasena)

    def obtener_por_email(self, email):
        return self.repository.obtener_por_email(email)

    def guardar_usuario(self, usuario):
        return self.repository.guardar_usuario(usuario)
