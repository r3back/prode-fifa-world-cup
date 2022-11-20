import requests
import json

from me.reb4ck.prode.MenuPronostico import MenuPronostico


class MenuProde():

    def mostrar_opciones(self, usuario, primera_vez):
        mensaje_personal = self.obtener_mensaje_personal(usuario, primera_vez)

        print(mensaje_personal)
        print("")
        print("[1] Crear pronostico ")
        print("[2] Ver mi pronostico ")
        print("[3] Cerrar Sesion")
        print("")

        respuesta = input("Ingrese una de las opciones: ")

        self.verificar_respuesta(respuesta)

    def obtener_mensaje_personal(self, usuario, primera_vez):
        if primera_vez:
            return "Bienvenido al prode del Mundial Qatar 2022 {nombre}!".replace("nombre", usuario.getNombre())
        else:
            return "Bienvenido de vuelta al prode del Mundial Qatar 2022 {nombre}!".replace("nombre", usuario.getNombre())

    def verificar_respuesta(self, respuesta):
        if respuesta == "1":
            MenuPronostico().crear_pronostico()




