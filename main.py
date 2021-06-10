from menudef import *
from tkinter import *
from exceldef import *

window = Tk()

window.title("NAVE DE GRAPAS")
window.geometry('1500x400')


def verproducc():
    height = 10
    width = 8
    ts = ver_sheets('EstadoProducc')
    j = 0
    i = 0
    for tsa in ts:
        for v in tsa:
            if v != None:
                bcolor = "blue"
                fcolor = "white"
                #b = Entry(window, width=10, background=bcolor, foreground=fcolor)
                b = Label(window, width=10, background=bcolor, foreground=fcolor,text='{:>10}'.format(v))
                b.grid(row=i + 3, column=20 + j)
                #b = Label(window, text='{:>10}'.format(v))
            else:
                i += 1
                break
            j += 1
        i += 1
        j = 0


#lbl = Label(window, text="AQUI")
#lbl.grid(column=5, row=20)
btn = Button(window, text="VER PRODUCCIÓN", command=verproducc)
btn.grid(column=1, row=0)

menubar = creamenu(window)
window.config(menu=menubar)

window.mainloop()
