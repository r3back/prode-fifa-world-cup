class User:
    def __init__(self, nombre, email, contrasena, datos):
        self.contrasena = contrasena
        self.nombre = nombre
        self.email = email
        self.datos = datos

    def getDatos(self):
        return self.datos

    def getNombre(self):
        return self.nombre

    def getEmail(self):
        return self.email

    def getContrasena(self):
        return self.contrasena

    def add_datos(self, datos):
        self.datos += datos

    def get_user_prode(self, equipo_local, equipo_visitante):
        for prode in self.datos:
            if prode.equipo_local == equipo_local and prode.equipo_visitante == equipo_visitante:
                return prode
        return None


class UserProde:
    def __init__(self, equipo_local, equipo_visitante, equipo_local_goles, equipo_visitante_goles):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.equipo_local_goles = equipo_local_goles
        self.equipo_visitante_goles = equipo_visitante_goles
