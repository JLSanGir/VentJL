from datetime import *
from tkinter import ttk
from exceldef import *
from menudef import *
import re


class Aplicacion():
    ventana = 0
    posx_y = 0

    def __init__(self):
        ''' Construye la ventana  principal aplicación '''

        self.raiz = Tk()
        self.raiz.geometry('800x300')
        self.raiz.resizable(True, True)
        fecha_actualizado = ver_celda("Grapas - Corte de varilla", 2, 1)
        self.raiz.title("NAVE DE GRAPAS  Actualizado a " + fecha_actualizado.strftime('%d %b %Y'))

        self.mmat = [["" for x in range(8)] for y in range(10)]
        self.verproducc()

        menubar = creamenu(self.raiz)
        self.raiz.config(menu=menubar)
        self.m = Menu(self.raiz, tearoff=0)
        self.m.add_command(label="Historial temperaturas", command=lambda: self.abrir("Temperaturas"))
        self.m.add_command(label="Copy")
        self.raiz.mainloop()

    def abrir(self, titulo):
        ''' Construye una ventana de diálogo '''
        self.dialogo = Toplevel()
        Aplicacion.ventana += 1
        Aplicacion.posx_y += 50
        tamypos = '300x300+' + str(Aplicacion.posx_y) + '+' + str(Aplicacion.posx_y)
        self.dialogo.geometry(tamypos)
        self.dialogo.resizable(True, True)
        ident = self.dialogo.winfo_id()

        titulo = str(Aplicacion.ventana) + " " + titulo
        self.dialogo.title(titulo)
        boton = ttk.Button(self.dialogo, text='Cerrar',
                           command=self.dialogo.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        self.raiz.wait_window(self.dialogo)

    def verproducc(self):
        height = 10
        width = 8
        self.pon_tit()
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
                        b = Label(self.raiz, width=10, background=bcolor, foreground=fcolor, text='{:>10}'.format(v),
                                  borderwidth=2, relief="groove")
                        self.mmat[i][j] = v
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

    def handle_click(self, texto):
        act = re.findall(r"R\d+", texto)
        ac1 = act[0].replace("R", "")
        ac = int(ac1)
        act = re.findall(r"C\d+", texto)
        ac2 = act[0].replace("C", "")
        bc = int(ac2)
        print(texto, ac1, ac2)
        tt = self.mmat[ac - 3][bc]
        b = Label(self.raiz, width=10, background="yellow", foreground="black",
                  text='{:>10}'.format(tt), borderwidth=2, relief="solid").grid(row=ac, column=bc)

    def do_popup(self, event):
        try:
            self.m.tk_popup(event.x_root, event.y_root)
        finally:
            self.m.grab_release()

    def pon_tit(self):
        titulos = ('-COLADA-', 'TIPO', 'CORTE VAR.', 'URP', 'HORNO', 'INSPECCIÓN', 'PINTURA', 'EXPEDIDOS')
        for i in range(len(titulos)):
            lbl = Label(self.raiz, width=10, background='yellow', foreground='black', text=titulos[i],
                        borderwidth=2, relief="groove")
            lbl.grid(column=i, row=1)
