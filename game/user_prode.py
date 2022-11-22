import string


class UserProde:
    def __init__(self, equipo_local: string, equipo_visitante: string, equipo_local_goles: string,
                 equipo_visitante_goles: string, email_enviado):
        self.equipo_local = equipo_local
        self.email_enviado = email_enviado
        self.equipo_visitante = equipo_visitante
        self.equipo_local_goles = equipo_local_goles
        self.equipo_visitante_goles = equipo_visitante_goles

    def encode(self):
        return self.__dict__
