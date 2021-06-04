from menudef import *
from tkinter import *
from exceldef import *


window = Tk()

window.title("NAVE DE GRAPAS")
window.geometry('600x400')

def clicked():
    lbl.configure(text=texto)
    height = 5
    width = 5
    for i in range(height): #Rows
        for j in range(width): #Columns
            b = Entry(window, text=type(lista_sheets))
            b.grid(row=i, column=j)

ts = ver_sheets()
tsa = ts[1]
lbl = Label(window, text=tsa)
lbl.grid(column=5, row=20)
btn = Button(window, text="Pulsame", command=clicked)
btn.grid(column=1, row=0)

menubar = creamenu(window)
window.config(menu=menubar)


window.mainloop()

