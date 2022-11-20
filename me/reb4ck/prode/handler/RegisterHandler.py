from me.reb4ck.prode.MenuPronostico import MenuPronostico
from me.reb4ck.prode.service.UserService import UserService
from me.reb4ck.prode.user.User import User

class RegisterHandler:
    @staticmethod
    def registrarse():
        nombre = input("Ingresa tu Nombre: ")
        email = input("Ingresa tu email: ")
        contrasena = input("Ingresa tu contraseña: ")

        usuario = User(nombre, email, contrasena, [])

        if RegisterHandler.usuario_existe(usuario):
            print("Ya existe un usuario con ese email!")
            RegisterHandler.registrarse()
        else:
            UserService.get_instance().guardar_usuario(usuario)
            print("Usuario registrado correctamente!")
            MenuPronostico.crear_pronostico()

    @staticmethod
    def usuario_existe(usuario):
        return UserService.get_instance().obtener_por_email(usuario.email) is not None
