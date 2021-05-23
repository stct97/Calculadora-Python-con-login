from tkinter import *
from math import *
from tkinter import messagebox
import sqlite3


loginWindow = Tk()
loginWindow.title("          Introduzca datos!          ")
loginWindow.geometry("350x150+500+250")
Label(loginWindow, text="Usuario:").pack()
caja1 = Entry(loginWindow)
caja1.pack()

Label(loginWindow, text="Contraseña:").pack()
caja2 = Entry(loginWindow, show="*")
caja2.pack()

# CONEXION A LA BD
db = sqlite3.connect('/Users/Usuario/Desktop/PT20/login.db')
db.execute("insert into usuarios(usuario,pass) values('root','123456')")


def login():

    c = db.cursor()

    usuario = caja1.get()
    contr = caja2.get()

    c.execute('SELECT * FROM usuarios WHERE usuario = ? AND pass = ?',
              (usuario, contr))

    if c.fetchone():
        loginWindow.destroy()                 
    else:
        messagebox.showerror(title="Login incorrecto",
                             message="Usuario o contraseña incorrecta")

    c.close()


Button(text="Login", command=login).pack()


loginWindow.mainloop()
