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
    tamypos = '800x300+' + str(posx_y) + '+200'
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

    print(type(lst_col))
    print(type(lst_col[1]))
    print(lst_col[1])
    colad = "F-123456"
    print(type(colad))
    print(colad)
    datos = {}
    # datos = { i : lst_col[i] for i in range(1, len(lst_col))}
    ii = 0
    for colada in lst_col:
        #colad = str((re.findall(r"[A-Z]-\d+", str(colada))))
        #print(type(colada))
        print(str(colada) + ",   indice: " + str(ii) + ": " + str(lst_col[ii]))
        #colada = colada.replace("(", "")
        if ii>0 :
            datos[lst_col[ii]] = ["01/01/2000", 0]
        #datos.setdefault(colad, ["01/01/2000", 0])
        ii += 1
    #for c in lst_col:
    #    ii = lst_col.index(str(c))
    #    datos[c] = [c[lst_fec[ii], lst_can[ii]]]

    print(lst_col)
    print(lst_fec)
    print(lst_col[2])
    print(datos)

    datos[lst_col[2]] = ["01/01/2021", 1111]
    print(datos)


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
