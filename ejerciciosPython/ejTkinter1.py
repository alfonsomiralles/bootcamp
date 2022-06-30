from cgitb import text
from tkinter import *
import tkinter

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
tkinter.Label(root, 
        text="""Choose a Warrior:""",
        justify = tkinter.LEFT,
        padx = 20).pack()

v = tkinter.IntVar()
v.set(1)
warriors = [("Goku", 101),
   	     ("Vegeta", 102),
    	     ("Gohan", 103),
             ("Krilin", 104),
             ("Broly", 105)]

for warrior, val in warriors:
    tkinter.Radiobutton(root, 
                   text=warrior,
                   padx = 20, 
                   variable=opcion, 
                   command=seleccionar,
                   value=warrior).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()