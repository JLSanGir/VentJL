import re
from tkinter import *
from ventana import *
from exceldef import *
import datetime


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

    datosCol = {}
    # datos = { i : lst_col[i] for i in range(1, len(lst_col))}
    ii = 0
    # print(lst_fec)
    for ii in range(1, f):
        if lst_col[ii] in datosCol:
            try:
                datetime.datetime.strptime(str(lst_fec[ii]), '%d/%m/%Y')
                v = int(datosCol.get(lst_col[ii])[1]) + int(lst_can[ii])
                datosCol[lst_col[ii]] = [lst_fec[ii], v]
            except ValueError:
                print(lst_fec[ii])
        else:
            try:
                datetime.datetime.strptime(str(lst_fec[ii]), '%d/%m/%Y')
                datosCol[lst_col[ii]] = [lst_fec[ii], int(lst_can[ii])]
            except ValueError:
                print(lst_fec[ii])

    print(lst_col[2])
    print(datosCol)
    dict(sorted(datosCol.items(), key=lambda item: item[1], reverse=False))
    print("............")
    print(list(datosCol.items())[0][0])
    print(list(datosCol.values())[1][0])
    print(type(list(datosCol.values())[2][0]))
    # print(type(datos.values(2)))
    # datos(lst_col[2]) = 2222
    # datosCol[lst_col[2]] = ["01/01/2021", 1111]
    print(datosCol[lst_col[2]])
    print(datosCol)

    fcolor = "white"
    j = 0  # filas
    bcolor = "blue"
    i = 0  # columnas
    lcoladas = []

    dat = []
    for v in datosCol:  # .values():
        text = 'R%s/C%s' % (i + 3, j)
        dat.append(v)
        b1 = Label(filewin, height=1, width=15, background=bcolor, foreground=fcolor, text=v,
                   borderwidth=2, relief="groove")
        b2 = Label(filewin, height=1, width=10, background=bcolor, foreground=fcolor, text=datosCol[v][0],
                   borderwidth=2, relief="groove")
        b1.grid(row=i + 3, column=j)
        b2.grid(row=i + 3, column=j + 1)

        b1.bind('<Button-1>', lambda e, text=text: cambia_color(filewin, text, dat))
        filewin.update()
        # b1.bind('<Button-1>', lambda e, text=text1: cambia_color(text1))


        # b1.bind("<Button-3>", self.do_popup)

        i += 1


def cambia_color(filewin, coorde, dat):
    print(coorde)
    act = re.findall(r"R\d+", coorde)
    ac1 = act[0].replace("R", "")
    ac = int(ac1)
    act = re.findall(r"C\d+", coorde)
    ac2 = act[0].replace("C", "")
    bc = int(ac2)

    tt = dat[ac]
    #tcolada = self.mmat[ac - 3][0]
    b = Label(filewin, width=10, background="yellow", foreground="black",
              text='{:>10}'.format(tt), borderwidth=2, relief="solid")
    b.grid(row=ac, column=bc)


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
