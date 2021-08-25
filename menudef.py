from tkinter import *
from ventana import *


def donothing(window):
    filewin = Toplevel(window)
    button = Button(filewin, text="Botón para definir")
    button.pack()

def coladasAnteriores(window):
    ''' Construye una ventana de diálogo '''

    filewin = Toplevel(window)

    posx_y = 50
    tamypos = '800x300+' + str(posx_y) + '+200'
    filewin.geometry(tamypos)
    filewin.resizable(True, True)
    ident = filewin.winfo_id()

    titulo = "COLADAS TERMINADAS"
    filewin.title(titulo)
    boton = Button(filewin, text='Cerrar', command=filewin.destroy)
    boton.pack(side=BOTTOM, padx=20, pady=20)

    #raiz.wait_window(filewin)

def creamenu(window):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Coladas terminadas", command=lambda: coladasAnteriores(window))
    filemenu.add_command(label="Open", command=lambda :donothing(window))
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)

    menubar.add_cascade(label="File", menu=filemenu)
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=donothing)

    editmenu.add_separator()

    editmenu.add_command(label="Cut", command=donothing)

    menubar.add_cascade(label="Edit", menu=editmenu)
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)

    return menubar