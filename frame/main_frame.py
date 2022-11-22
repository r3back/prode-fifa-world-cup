from tkinter import Tk, Button, Label
from tkinter import Frame

from me.reb4ck.prode.config.ImageLoader import ImageLoader
from me.reb4ck.prode.frame.Login import Login
from me.reb4ck.prode.frame.Register import Register


class Main(Frame):
    executing = False

    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.widgets()

    def salir(self):
        self.master.destroy()
        self.master.quit()

    def iniciar_sesion(self):
        self.master.destroy()
        Login.iniciar_sesion()


    def registrarse(self):
        self.master.destroy()
        Register.registrarse()

    def widgets(self):
        self.logo = ImageLoader.get_image_from_file("logo.png")
        Label(self.master, image=self.logo, bg='firebrick', height=150, width=150).pack()

        self.logo2 = ImageLoader.get_image_from_file("mascota.png")
        Label(self.master, image=self.logo2, bg='firebrick', height=200, width=200).pack()

        Button(self.master, text='Iniciar Sesion', command=self.iniciar_sesion, activebackground='white',
               bg='#FBAD80', font=('Arial', 12, 'bold')).pack(pady=10)
        Button(self.master, text='Registrarse', command=self.registrarse, activebackground='white',
               bg='#FBAD80', font=('Arial', 12, 'bold')).pack(pady=10)
        Button(self.master, text='Salir', bg='firebrick', activebackground='firebrick', bd=0, fg='black',
               font=('Lucida Sans', 15, 'italic'), command=self.salir).pack(pady=10)

    @staticmethod
    def open():
        ventana = Tk()
        ventana.config(bg='firebrick')
        ventana.geometry('350x530+500+50')
        ventana.overrideredirect(1)
        ventana.resizable(0, 0)
        app = Main(ventana)
        app.mainloop()