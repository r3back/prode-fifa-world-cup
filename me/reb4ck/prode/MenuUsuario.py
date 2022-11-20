from tkinter import *
from tkinter import ttk

from me.reb4ck.prode.api.ExternalProdeAPI import ExternalProdeAPI
from me.reb4ck.prode.config.DecorationConfigLoader import DecorationConfigLoader
from me.reb4ck.prode.handler.LoginHandler import LoginHandler
from me.reb4ck.prode.handler.RegisterHandler import RegisterHandler


class ProdeMundial:
    def bienvenida_usuario(self):
        for line in DecorationConfigLoader.get_ascii_config("pelota"):
            print(line)

        print("Bienvenido al Prode del Mundial Qatar 2022")
        print("")
        print("[1] Iniciar Sesion")
        print("[2] Registrarse")
        print("")

        respuesta = input("Ingrese una de las opciones: ")

        self.verificar_respuesta(respuesta)

    def verificar_respuesta(self, respuesta):
        if respuesta == "1":
            LoginHandler.iniciar_sesion()
        elif respuesta == "2":
            RegisterHandler.registrarse()
        else:
            print()

def saludo():
    print("hola")

#ExternalProdeAPI.get_instance().descargar()
#ProdeMundial().bienvenida_usuario()
raiz = Tk()

mi_frame = Frame(raiz, width=1200, height=600)
mi_frame.pack()

cuadro_nombre = Entry(mi_frame)
cuadro_nombre.grid(row=0, column=1, padx=30, pady=20)
cuadro_nombre.config(fg="black", justify="left")

cuadro_email = Entry(mi_frame)
cuadro_email.grid(row=1, column=1, padx=30, pady=20)
cuadro_email.config(fg="black", justify="left")

cuadro_contrasena = Entry(mi_frame)
cuadro_contrasena.grid(row=2, column=1, padx=30, pady=20)
cuadro_contrasena.config(fg="black", justify="left")


label_nombre = Label(mi_frame, text="Nombre")
label_nombre.grid(row=0, column=0, padx=10, pady=20)

label_email = Label(mi_frame, text="Email")
label_email.grid(row=1, column=0, padx=10, pady=20)

label_contrasena = Label(mi_frame, text="Contraseña")
label_contrasena.grid(row=2, column=0, padx=10, pady=20)


photo = PhotoImage(file =r"frame/login/logo.png")

action = ttk.Button(raiz, text="Registrarse", default="active", command=saludo, image=photo)
action.pack()
#action.place(x=50, y=50)

raiz.bind('<Return>', lambda e: action.invoke())

raiz.mainloop()

