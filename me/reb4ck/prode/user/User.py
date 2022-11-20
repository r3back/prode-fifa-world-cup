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
