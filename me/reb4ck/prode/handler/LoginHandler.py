from me.reb4ck.prode.MenuPronostico import MenuPronostico
from me.reb4ck.prode.service.UserService import UserService


class LoginHandler:
    @staticmethod
    def iniciar_sesion():
        email = input("Ingresa tu email:")
        contrasena = input("Ingresa tu contraseña:")

        usuario = UserService.get_instance().obtener_por_email_y_contraseña(email, contrasena)

        if usuario is None:
            print("No existe ningun usuario con esa combinacion de email y contraseña!")
            LoginHandler.iniciar_sesion()
        else:
            LoginHandler.validar_inicio_de_sesion(usuario)

    @staticmethod
    def validar_inicio_de_sesion(usuario):
        MenuPronostico.crear_pronostico()
