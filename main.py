from menudef import *
from tkinter import *
from exceldef import *

window = Tk()

window.title("NAVE DE GRAPAS")
window.geometry('1600x400')


def clicked():
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
                b = Entry(window, width=10, background=bcolor, foreground=fcolor)
                b.grid(row=i + 30, column=20 + j)
                b.insert(0, '{:>10}'.format(v))
            else:
                i += 1
                break
            j += 1
        i += 1
        j = 0




lbl = Label(window, text="")
lbl.grid(column=5, row=20)
btn = Button(window, text="Pulsame", command=clicked)
btn.grid(column=1, row=0)

menubar = creamenu(window)
window.config(menu=menubar)

window.mainloop()
