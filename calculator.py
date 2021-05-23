from tkinter import *
from math import *
from tkinter import messagebox
import login

# DATOS PARA OPERAR


def btnClik(num):
    global operador
    operador = operador+str(num)
    input_text.set(operador)

# OPERACION Y RESULTADO, LANZA VENTANA DE DIALOGO EN CASO DE OPERACIONES


def result():
    global operador
    try:
        opera = str(eval(operador))
        input_text.set(opera)
    except:
        messagebox.showinfo(
            message="No ha realizado operaciones válidas", title="Error 502")
    operador = " "

# LIMPIEZA


def clear():
    global operador
    operador = (" ")
    input_text.set("0")


def askQuit():
    if messagebox.askokcancel("Cerrar la aplicación", "¿Seguro que quieres cerrar la aplicación?\n\n Se perderan todos los resultados"):
        window.destroy()


window = Tk()

withWindow = 392
heightWindow = 600
xWindow = window.winfo_screenmmwidth()
yWindow = window.winfo_screenmmheight()
position = str(withWindow) + "x" + str(heightWindow) + \
    "+" + str(xWindow) + "+" + str(yWindow)
window.resizable(0, 0)
window.geometry(position)
window.configure(background="white")
window.title("CALCULATOR")
window.iconbitmap("calculator_3534.ico")

colorBtn = ("snow2")
withBtn = 11
heightBtn = 3

input_text = StringVar()

operador = " "
output = Entry(window, font=('arial', 20, 'bold'), width=22,
               textvariable=input_text, bd=20, insertwidth=4, bg="powder blue", justify="right")
output.place(x=10, y=60)

# CREAMOS NUESTROS BOTONES
Button(window, text="0", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(0)).place(x=17, y=180)
Button(window, text="1", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(1)).place(x=107, y=180)
Button(window, text="2", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(2)).place(x=197, y=180)
Button(window, text="3", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(3)).place(x=287, y=180)
Button(window, text="4", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(4)).place(x=17, y=240)
Button(window, text="5", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(5)).place(x=107, y=240)
Button(window, text="6", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(6)).place(x=197, y=240)
Button(window, text="7", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(7)).place(x=287, y=240)
Button(window, text="8", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(8)).place(x=17, y=300)
Button(window, text="9", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(9)).place(x=107, y=300)
Button(window, text="π", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("pi")).place(x=197, y=300)
Button(window, text=",", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(".")).place(x=287, y=300)
Button(window, text="+", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("+")).place(x=17, y=360)
Button(window, text="-", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("-")).place(x=107, y=360)
Button(window, text="*", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("*")).place(x=197, y=360)
Button(window, text="/", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("/")).place(x=287, y=360)
Button(window, text="√", bg=colorBtn, width=withBtn, height=heightBtn,
       command=lambda: btnClik("sqrt(")).place(x=17, y=420)
Button(window, text="(", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("(")).place(x=17, y=480)
Button(window, text=")", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik(")")).place(x=107, y=480)
Button(window, text="%", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("%")).place(x=197, y=480)
Button(window, text="ln", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("log(")).place(x=287, y=480)
Button(window, text="C", bg=colorBtn, width=withBtn,
       height=heightBtn, command=clear).place(x=107, y=420)
Button(window, text="EXP", bg=colorBtn, width=withBtn,
       height=heightBtn, command=lambda: btnClik("**")).place(x=197, y=420)
Button(window, text="=", bg=colorBtn, width=withBtn,
       height=heightBtn, command=result).place(x=287, y=420)

clear()

window.protocol("WM_DELETE_WINDOW", askQuit)
window.mainloop()
