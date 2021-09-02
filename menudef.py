import re
from tkinter import *
from ventana import *
from exceldef import *


def donothing(window):
    filewin = Toplevel(window)
    button = Button(filewin, text="Botón para definir")
    button.pack()


def coladasAnteriores(window, titulo):
    ''' Construye una ventana de diálogo '''

    filewin = Toplevel(window)

    posx_y = 50
    tamypos = '400x800+' + str(posx_y) + '+200'
    filewin.geometry(tamypos)
    filewin.resizable(True, True)
    ident = filewin.winfo_id()

    filewin.title(titulo)
    ts1, f = ver_sheets("Grapas - Pintura", 67, 67)
    lst_col = []
    for t in ts1:
        for x in t:
            lst_col.append(x)

    ts2, f = ver_sheets("Grapas - Pintura", 7, 7)
    lst_fec = []
    for t in ts2:
        for x in t:
            lst_fec.append(x)

    ts3, f = ver_sheets("Grapas - Pintura", 24, 24)
    lst_can = []
    for t in ts3:
        for x in t:
            lst_can.append(x)

    datos = {}
    # datos = { i : lst_col[i] for i in range(1, len(lst_col))}
    ii = 0
    # print(lst_fec)
    for ii in range(1, f):
        if lst_col[ii] in datos:
            print(datos.get(lst_col[ii])[1])
            print(lst_can[ii])
            v = int(datos.get(lst_col[ii])[1]) + int(lst_can[ii])
            # v = 0
            datos[lst_col[ii]] = [lst_fec[ii], v]
        else:
            datos[lst_col[ii]] = [lst_fec[ii], int(lst_can[ii])]

    print(lst_col[2])
    print(datos)
    print(list(datos.items())[2])
    print(list(datos.values())[2][1])
    # print(type(datos.values(2)))
    # datos(lst_col[2]) = 2222
    datos[lst_col[2]] = ["01/01/2021", 1111]
    print(datos[lst_col[2]])
    print(datos)

    fcolor = "white"
    j = 0  # filas
    bcolor = "blue"
    i = 0  # columnas

    frame = Frame( filewin,bg='#A8B9BF')
    text_box = Text(filewin,height=13,width=32,font=(12))
    text_box.grid(row=0, column=0)
    text_box.config(bg='#D9D8D7')
    scrollbar = Scrollbar(filewin, orient=VERTICAL)
    scrollbar.grid(row=0, column=1, sticky=NS)
    text_box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text_box.yview)

    for v in datos:
        b = Label(filewin, width=20, background=bcolor, foreground=fcolor, text=v,
                  borderwidth=2, relief="groove")
        b.grid(row=i + 3, column=j)
        i += 1


def creamenu(window):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Coladas terminadas", command=lambda: coladasAnteriores(window, "COLADAS TERMINADAS"))
    filemenu.add_command(label="Open", command=lambda: donothing(window))
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
