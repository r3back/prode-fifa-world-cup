from tkinter import Tk, Button, Label, Frame, Toplevel

from loader.image_loader import ImageLoader
from frame.login_frame import Login
from frame.register_frame import Register


class Main(Frame):
    executing = False

    def __init__(self, *args):
        super().__init__(Tk(), *args)
        self.master.config(bg='firebrick')
        self.master.geometry('350x530+500+50')
        self.master.overrideredirect(1)
        self.master.resizable(0, 0)
        self.widgets()
        self.master.mainloop()

    def salir(self):
        self.master.destroy()
        self.master.quit()

    def iniciar_sesion(self):
        self.master.destroy()
        Login()


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