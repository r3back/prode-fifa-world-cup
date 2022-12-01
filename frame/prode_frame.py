import json
import math
import sys
from tkinter import Tk, Button, Entry, Label, Toplevel
from tkinter import Frame

from api.prode_api import ExternalProdeAPI
from game.user import User
from game.user_prode import UserProde
from loader.image_loader import ImageLoader
import tkinter as tk

from service.user_service import UserService


class Prode(Frame):
    executing = False
    goles_visitante_texto = {}
    goles_local_texto = {}
    banderas = {}
    messi_picture = None
    messi = None

    page = None
    has_next = None
    max_per_page = 15
    flags = True

    def __init__(self, usuario, *args):
        super().__init__()
        self.labels = []
        self.usuario = usuario
        self.matches = ExternalProdeAPI.get_matches()
        self.page_amount = self.getMaxPage()
        self.master = Toplevel()
        self.master.title('Fifa World Cup 2022 Qatar 2022 - Prode')
        self.master.geometry("1280x720")
        self.master.config(bg='firebrick')
        self.master.resizable(0, 0)
        self.widgets()
        self.set_matches(self.flags, 1)
        self.master.mainloop()

    def getMaxPage(self):
        return math.ceil(len(self.matches) / self.max_per_page)

    def salir(self):
        self.master.destroy()
        self.master.quit()
        sys.exit()

    def siguiente_pagina(self):
        if self.page >= self.page_amount:
            return None
        self.remove_all_from_page()
        self.set_matches(self.flags, self.page + 1)

    def anterior_pagina(self):
        if self.page == 1:
            return None
        self.remove_all_from_page()
        self.set_matches(self.flags, self.page - 1)

    def widgets(self):
        self.messi = ImageLoader.get_image_from_file("messi.png")
        Label(self.master, image=self.messi, bg='firebrick', height=500, width=289).place(x=25, y=180)

        self.mbappe = ImageLoader.get_image_from_file("mbappe.png")
        Label(self.master, image=self.mbappe, bg='firebrick', height=500, width=289).place(x=1000, y=180)

        self.logo = ImageLoader.get_image_from_file("logo.png")
        Label(self.master, image=self.logo, bg='firebrick', height=150, width=150).place(x=585)

        # Guardar Partidos

        Button(self.master, text='Guardar Resultados', command=self.guardar_resultados, activebackground='white',
               bg='#FBAD80', font=('Arial', 12, 'bold')).place(x=570, y=645)
        # Atras
        Button(self.master, text='Salir', command=self.salir, activebackground='white',
               bg='#FBAD80', font=('Arial', 12, 'bold')).place(x=630, y=682)

        # Anterior Pagina
        Button(self.master, text='<', command=self.anterior_pagina, activebackground='white',
               bg='#FBAD80', font=('Arial', 9, 'bold')).place(x=590, y=150)

        # Siguiente Pagina
        Button(self.master, text='>', command=self.siguiente_pagina, activebackground='white',
               bg='#FBAD80', font=('Arial', 9, 'bold')).place(x=700, y=150)

    def remove_all_from_page(self):
        for label in self.labels:
            label.destroy()
        self.labels = []

    def set_matches(self, flags, page):
        self.page = page

        self.remove_all_from_page()

        pady = 180
        cantidad = (self.max_per_page * self.page) - self.max_per_page

        paginacion = "Page {}/{}".format(str(self.page), str(int(self.page_amount)))

        # Pagina
        label = Label(self.master, text=paginacion, foreground="white", background="firebrick",
                      font=('Arial', 12, 'bold'))

        label.place(x=620, y=150)

        self.labels.append(label)

        for numero in range(0, 15):
            if cantidad >= 48:
                break

            partido = self.matches[cantidad]

            fecha = partido.fecha
            local = partido.equipo_local
            visitante = partido.equipo_visitante
            ya_fue_jugado = partido.ya_fue_jugado
            bandera_local = partido.bandera_local
            bandera_visitante = partido.bandera_visitante

            key = "{};{}".format(local, visitante)

            self.goles_visitante_texto[key] = tk.StringVar()
            self.goles_local_texto[key] = tk.StringVar()

            userprode = self.usuario.get_prode(local, visitante)

            self.status = tk.NORMAL

            if ya_fue_jugado is True:
                self.goles_visitante_texto[key].set("Terminado")
                self.goles_local_texto[key].set("Terminado")
                self.status = tk.DISABLED

            if userprode is not None:
                self.status = tk.DISABLED
                self.goles_visitante_texto[key].set(userprode.equipo_visitante_goles)
                self.goles_local_texto[key].set(userprode.equipo_local_goles)

            if flags:
                # Bandera Local
                self.banderas[local] = ImageLoader.get_image_from_url_resized(bandera_local, 30, 15)
                #self.banderas[local] = ImageLoader.get_image_from_file("foto.png")

                label = Label(self.master, image=self.banderas[local], bg='firebrick', height=15, width=30)
                label.place(x=450, y=pady)

                # Bandera Visitante
                self.banderas[visitante] = ImageLoader.get_image_from_url_resized(bandera_visitante, 30, 15)

                label = Label(self.master, image=self.banderas[visitante], bg='firebrick', height=15, width=30)
                label.place(x=850, y=pady)

            # Equipo Local
            label = Label(self.master, text=local, foreground="white", background="firebrick",
                          font=('Arial', 9, 'bold'))

            label.place(x=500, y=pady)

            self.labels.append(label)

            # Equipo visitante
            label = Label(self.master, anchor="w", text=visitante, foreground="white", background="firebrick",
                          font=('Arial', 9, 'bold'))

            label.place(x=750, y=pady)

            self.labels.append(label)

            # Goles Local
            goles_local = Entry(self.master, width=10, justify="center", textvariable=self.goles_local_texto[key],
                                state=self.status)

            goles_local.place(x=590, y=pady)

            self.labels.append(goles_local)

            # Goles vistantes
            goles_visitante = Entry(self.master, width=10, justify="center",
                                    textvariable=self.goles_visitante_texto[key],
                                    state=self.status)
            goles_visitante.place(x=660, y=pady)

            self.labels.append(goles_visitante)

            pady += 30
            cantidad += 1

    def get_user_prodes(self):
        user_prodes = []
        for key in self.goles_local_texto:
            split_key = key.split(";")

            local = split_key[0]
            visitante = split_key[1]

            if self.usuario.get_prode(local, visitante) is not None:
                continue

            goles_local = self.goles_local_texto[key].get()
            goles_visitante = self.goles_visitante_texto[key].get()

            if goles_local is None or goles_visitante is None or goles_local == "" or goles_visitante == "" or goles_local == "Terminado":
                continue

            user_prode = UserProde(local, visitante, goles_local, goles_visitante, "false", "-1", "-1")
            user_prodes.append(user_prode)

        return user_prodes

    def guardar_resultados(self):
        nuevos_prodes = self.get_user_prodes()

        if len(nuevos_prodes) == 0:
            return None

        self.usuario.add_prodes(nuevos_prodes)

        UserService.get_instance().save_user(self.usuario)

        for widget in self.master.winfo_children():
            widget.destroy()

        self.widgets()
