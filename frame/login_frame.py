from tkinter import Tk, Button, Entry, Label, ttk
from tkinter import END, HORIZONTAL, Frame
import time

from loader.image_loader import ImageLoader
from frame.prode_frame import Prode
from service.user_service import UserService


class Login(Frame):
    executing = False

    def __init__(self, *args):
        super().__init__(Tk(), *args)
        self.user_marcar = "Ingrese su correo"
        self.contra_marcar = "Ingrese su contraseña"
        self.fila1 = ''
        self.fila2 = ''
        self.master.config(bg='firebrick')
        self.master.geometry('350x500+500+50')
        self.master.overrideredirect(1)
        self.master.resizable(0, 0)
        self.widgets()
        self.master.mainloop()

    def entry_out(self, event, event_text):
        if event['fg'] == 'black' and len(event.get()) == 0:
            event.delete(0, END)
            event['fg'] = 'grey'
            event.insert(0, event_text)
        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = ""
        if self.entry2.get() != 'Ingrese su correo':
            self.entry2['show'] = "*"

    def entry_in(self, event):
        if event['fg'] == 'grey':
            event['fg'] = 'black'
            event.delete(0, END)

        if self.entry2.get() != 'Ingrese su contraseña':
            self.entry2['show'] = "*"

        if self.entry2.get() == 'Ingrese su contraseña':
            self.entry2['show'] = ""

    def salir(self):
        from frame.main_frame import Main
        self.master.withdraw()
        self.master.destroy()
        self.master.quit()
        Main()

    def join_prode_frame(self):
        #for i in range(101):
        #    self.barra['value'] += 1
        #    self.master.update()
         #   time.sleep(0.02)
        self.master.withdraw()
        Prode(self.usuario)

    def check_access(self):
        self.indica1['text'] = ''
        self.indica2['text'] = ''
        users_entry = self.entry1.get()
        password_entry = self.entry2.get()

        if users_entry != self.user_marcar or self.contra_marcar != password_entry:
            if self.executing:
                return None

            users_entry = users_entry
            password_entry = password_entry

            self.usuario = UserService.get_instance().get_user_by_email_and_password(users_entry, password_entry)

            dato1 = "dato1"
            dato2 = "dato2"

            self.fila1 = dato1
            self.fila2 = dato2

            if self.usuario is None:
                self.indica2['text'] = 'Contraseña incorrecta'
                self.indica1['text'] = 'Email incorrecto'
            else:
                self.executing = True
                self.join_prode_frame()

    def widgets(self):
        self.logo = ImageLoader.get_image_from_file("logo.png")
        Label(self.master, image=self.logo, bg='firebrick', height=150, width=150).pack()
        Label(self.master, text='Email', bg='firebrick', fg='black', font=('Lucida Sans', 16, 'bold')).pack(pady=5)
        self.entry1 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey',
                            highlightbackground="#5A0410",
                            highlightcolor="#B3031C", highlightthickness=5)
        self.entry1.insert(0, self.user_marcar)
        self.entry1.bind("<FocusIn>", lambda args: self.entry_in(self.entry1))
        self.entry1.bind("<FocusOut>", lambda args: self.entry_out(self.entry1, self.user_marcar))
        self.entry1.pack(pady=4)

        self.indica1 = Label(self.master, bg='firebrick', fg='black', font=('Arial', 8, 'bold'))
        self.indica1.pack(pady=2)

        # contraseña y entry
        Label(self.master, text='Contraseña', bg='firebrick', fg='black', font=('Lucida Sans', 16, 'bold')).pack(
            pady=5)
        self.entry2 = Entry(self.master, font=('Comic Sans MS', 12), justify='center', fg='grey',
                            highlightbackground="#5A0410",
                            highlightcolor="#B3031C", highlightthickness=5)
        self.entry2.insert(0, self.contra_marcar)
        self.entry2.bind("<FocusIn>", lambda args: self.entry_in(self.entry2))
        self.entry2.bind("<FocusOut>", lambda args: self.entry_out(self.entry2, self.contra_marcar))
        self.entry2.pack(pady=4)
        self.indica2 = Label(self.master, bg='firebrick', fg='black', font=('Arial', 8, 'bold'))
        self.indica2.pack(pady=2)
        Button(self.master, text='Iniciar Sesion', command=self.check_access, activebackground='white',
               bg='#FBAD80', font=('Arial', 12, 'bold')).pack(pady=10)
        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TProgressbar", foreground='red', background='#31B003', troughcolor='firebrick',
                         bordercolor='#FDFDFD', lightcolor='#42D90B', darkcolor='black')
        self.barra = ttk.Progressbar(self.master, orient=HORIZONTAL, length=200, mode='determinate', maximum=100,
                                     style="TProgressbar")
        self.barra.pack()
        Button(self.master, text='Atras', bg='firebrick', activebackground='firebrick', bd=0, fg='black',
               font=('Lucida Sans', 15, 'italic'), command=self.salir).pack(pady=10)


