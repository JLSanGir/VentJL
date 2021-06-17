from tkinter import *
from tkinter import ttk
from exceldef import *
from menudef import *

class Aplicacion():
    ventana = 0
    posx_y = 0

    def __init__(self):
        ''' Construye la ventana  principal aplicación '''

        self.raiz = Tk()
        self.raiz.title("NAVE DE GRAPAS")
        self.raiz.geometry('800x300')

        self.raiz.resizable(0, 0)
        titulos = ('COLADA', 'TIPO', 'CORTE VAR.', 'URP', 'HORNO', 'INSPECCIÓN', 'PINTURA', 'EXPEDIDOS')
        for i in range(len(titulos)):
            lbl = Label(self.raiz, width=10, background='yellow', foreground='black', text=titulos[i])
            lbl.grid(column=i, row=1)
        self.verproducc()

        menubar = creamenu(self.raiz)
        self.raiz.config(menu=menubar)

        self.m = Menu(self.raiz, tearoff=0)
        self.m.add_command(label="Historial temperaturas", command=self.abrir)
        self.m.add_command(label="Más")
        self.m.add_command(label="Paste")
        self.m.add_command(label="Reload")
        self.m.add_separator()
        self.m.add_command(label="Rename")

        self.raiz.mainloop()

    def abrir(self):
        ''' Construye una ventana de diálogo '''
        self.dialogo = Toplevel()
        Aplicacion.ventana += 1
        Aplicacion.posx_y += 50
        tamypos = '300x300+' + str(Aplicacion.posx_y) + '+' + str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(True, True)
        ident = self.dialogo.winfo_id()

        titulo = str(Aplicacion.ventana) + " " + str(ident)
        self.dialogo.title(titulo)
        boton = ttk.Button(self.dialogo, text='Cerrar',
                           command=self.dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        self.raiz.wait_window(self.dialogo)

    def verproducc(self):
        height = 10
        width = 8
        ts, filas = ver_sheets('EstadoProducc')
        j = 0  # filas
        i = 0  # columnas
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
                    if v != 0 and j < 8:
                        text = 'R%s/C%s' % (i + 3, j)
                        b = Label(self.raiz, width=10, background=bcolor, foreground=fcolor, text='{:>10}'.format(v))
                        b.grid(row=i + 3, column=j)
                        b.bind('<Button-1>', lambda e, text=text: self.handle_click(text))
                        b.bind("<Button-3>", self.do_popup)
                else:
                    salef = True
                    i += 1
                    break
                j += 1
            if salef:
                break
            i += 1
            j = 0
    def mouseClick(self, event):
        print("mouse clicked x= {}, y = {}".format(event.x,event.y))

    def handle_click(self, text):
        print(text)

    def do_popup(self, event):
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()