import tkinter
from tkinter import StringVar, OptionMenu
from IA import *

ventana = tkinter.Tk()

global est_orig, est_dest 

etiqueta = tkinter.Label(ventana, text="Bienvenido al metro de Kiev")
etiqueta.grid(row=0, column=1)

etiqueta2 = tkinter.Label(ventana, text="Seleccione su estación de origen")
etiqueta2.grid(row=5, column=0)

etiqueta2 = tkinter.Label(ventana, text="Seleccione su estación destino")
etiqueta2.grid(row=5, column=2)

def obtenerOrigen():
    est_orig = equiv2[origen.get()]
    return est_orig
    
def obtenerDestino():    
    est_dest = equiv2[destino.get()]
    return est_dest

def mostrarResultado():
    ventana2=tkinter.Tk()
    alg=algoritmo_a_estrella(obtenerOrigen(),obtenerDestino())
    ster="";
    for i in alg:
        ster=ster+str(i)+": "+equiv[i]+"\n | \n V \n"
    ster=ster+"Ha llegado a su destino"
    etiqueta = tkinter.Label(ventana2, text=ster)
    etiqueta.pack();

origen=StringVar()
origen.set("110: Akademmistechko")

w = OptionMenu(ventana, origen, *equiv2.keys())
w.grid(row=10, column=0)

destino=StringVar()
destino.set("110: Akademmistechko")

w2 = OptionMenu(ventana, destino, *equiv2.keys())
w2.grid(row=10, column=2)

boton = tkinter.Button(ventana, text="Averiguar la ruta óptima", command= lambda: mostrarResultado())
boton.grid(row=15, column=1)

ventana.mainloop()

