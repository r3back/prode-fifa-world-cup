from tkinter import Tk, Button, Entry, Label
from tkinter import Frame

from me.reb4ck.prode.config.ImageLoader import ImageLoader
from me.reb4ck.prode.service.ProdeAPIService import ProdeAPIService
import tkinter as tk

from me.reb4ck.prode.service.UserService import UserService
from me.reb4ck.prode.user.UserProde import UserProde


class Prode(Frame):
    executing = False
    goles_visitante_texto = {}
    goles_local_texto = {}

    def __init__(self, usuario, master, *args):
        super().__init__(master, *args)

        self.messi_picture = None
        self.messi = None
        self.master.title('Fifa World Cup 2022 Qatar 2022 - Prode')
        self.master.geometry("1280x720")
        self.master.config(bg='firebrick')
        self.master.resizable(0, 0)
        self.usuario = usuario
        self.widgets()

    def salir(self):
        self.master.destroy()
        self.master.quit()

    def widgets(self):
        # row = 4
        # initial_column = 115

        self.messi_picture = ImageLoader.get_image_from_file("messi.png")

        self.messi = Label(self.master, image=self.messi_picture, bg='firebrick', height=500, width=289)

        self.messi.place(x=25, y=180)

        self.mbappe = ImageLoader.get_image_from_file("mbappe.png")
        Label(self.master, image=self.mbappe, bg='firebrick', height=500, width=289).place(x=1000, y=180)

        # for numero in range(0, initial_column):
        #    Label(self.master, background="firebrick").grid(row=1, column=numero)

        self.logo = ImageLoader.get_image_from_file("logo.png")
        Label(self.master, image=self.logo, bg='firebrick', height=150, width=150).place(x=585)

        #self.mascota = ImageLoader.get_image_from_file("mascota.png")
        #Label(self.master, image=self.mascota, bg='firebrick', height=150, width=150).pack(side="top")

        pady = 180
        cantidad = 0
        for partido in ProdeAPIService.obtener_partidos():
            if cantidad == 15:
                break

            if partido.ya_fue_jugado:
                continue

            fecha = partido.fecha
            local = partido.equipo_local
            visitante = partido.equipo_visitante

            key = "{};{}".format(local, visitante)

            self.goles_visitante_texto[key] = tk.StringVar()
            self.goles_local_texto[key] = tk.StringVar()

            userprode = self.usuario.get_user_prode(local, visitante)

            status = tk.NORMAL

            if userprode is not None:
                status = tk.DISABLED
                self.goles_visitante_texto[key].set(userprode.equipo_visitante_goles)
                self.goles_local_texto[key].set(userprode.equipo_local_goles)

            #Equipo Local
            Label(self.master, text=local, foreground="white", background="firebrick", font=('Arial', 9, 'bold')).place(x=500, y=pady)

            #Equipo visitante
            Label(self.master, anchor="w", text=visitante, foreground="white", background="firebrick", font=('Arial', 9, 'bold')).place(x=750, y=pady)

            #Goles Local
            goles_local = Entry(self.master, width=10, justify="center", textvariable=self.goles_local_texto[key], state=status)
            goles_local.place(x=590, y=pady)

            #Goles vistantes
            goles_visitante = Entry(self.master, width=10, justify="center", textvariable=self.goles_visitante_texto[key], state=status)
            goles_visitante.place(x=660, y=pady)

            pady += 30
            cantidad += 1

        #Guardar Partidos
        Button(self.master, text='Guardar Resultados', command=self.guardar_resultados, activebackground='white',
             bg='#FBAD80', font=('Arial', 12, 'bold')).place(x=570, y=pady + 15)

    def get_user_prodes(self):
        user_prodes = []
        for key in self.goles_local_texto:
            split_key = key.split(";")

            local = split_key[0]
            visitante = split_key[1]

            if self.usuario.get_user_prode(local, visitante) is not None:
                continue

            goles_local = self.goles_local_texto[key].get()
            goles_visitante = self.goles_visitante_texto[key].get()

            if goles_local is None or goles_visitante is None or goles_local == "" or goles_visitante == "":
                continue

            user_prode = UserProde(local, visitante, goles_local, goles_visitante)
            user_prodes.append(user_prode)

        return user_prodes

    def guardar_resultados(self):
        self.usuario.add_datos(self.get_user_prodes())

        for widget in self.master.winfo_children():
            widget.destroy()
        self.widgets()

        UserService.get_instance().guardar_usuario(self.usuario)

        #Prode.open(self.usuario)

    @staticmethod
    def open(usuario):
        ventana = Tk()
        app = Prode(usuario, ventana)
        app.mainloop()
