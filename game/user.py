import json


class User:
    def __init__(self, name, email, password, prodes):
        self.password = password
        self.name = name
        self.email = email
        self.prodes = prodes

    def get_prodes(self):
        return self.prodes

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_password(self):
        return self.password

    def add_prodes(self, prodes):
        self.prodes += prodes

    def get_prode(self, equipo_local, equipo_visitante):
        for prode in self.prodes:
            if prode.equipo_local == equipo_local and prode.equipo_visitante == equipo_visitante:
                return prode
        return None

    def get_serialized_prodes(self):
        return json.dumps(self.prodes, default=lambda o: o.encode(), indent=4)



