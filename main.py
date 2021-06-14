from menudef import *
from tkinter import *
from exceldef import *

window = Tk()

window.title("NAVE DE GRAPAS")
window.geometry('1500x400')


def verproducc():
    height = 10
    width = 8
    ts, filas = ver_sheets('EstadoProducc')
    print(filas)
    j = 0 #filas
    i = 0 #columnas
    salef = False
    for tsa in ts:
        for v in tsa:
            if v != None:
                bcolor = "blue"
                fcolor = "white"
                if v == 'Skl1':
                    bcolor = "green"
                if v == 'Skl12':
                    bcolor = "orange"
                if v != 'Skl12' and v != 'Skl1' and j == 1:
                    bcolor = "red"
                #b = Entry(window, width=10, background=bcolor, foreground=fcolor)
                if v != 0 and j < 8:
                    text = 'R%s/C%s'%(i+3,j)
                    b = Label(window, width=12, background=bcolor, foreground=fcolor,text='{:>10}'.format(v))
                    b.grid(row=i + 3, column=j)
                    b.bind('<Button-1>', lambda e, text=text:handle_click(text))
                #b = Label(window, text='{:>10}'.format(v))
            else:
                salef = True
                i += 1
                break
            j += 1
        if salef:
            break
        i += 1
        j = 0

def mouseClick(event):
    print("mouse clicked x= {}, y = {}".format(event.x,event.y))

def handle_click(text):
    print(text)

titulos = ('COLADA', 'TIPO', 'CORTE VAR.', 'URP', 'HORNO', 'INSPECCIÓN', 'PINTURA', 'EXPEDIDOS')
#lbl = Label(window, text="PRODUCCIÓN").grid(column=25, row=0)
for i in range(len(titulos)):
    lbl = Label(window,  width=12, background='yellow', foreground='black', text=titulos[i])
    lbl.grid(column=i, row=1)
#btn = Button(window, text="VER PRODUCCIÓN", command=verproducc)
#btn.grid(column=1, row=0)
verproducc()

menubar = creamenu(window)
window.config(menu=menubar)

window.mainloop()
