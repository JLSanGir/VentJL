from tkinter import *

def donothing(window):
    filewin = Toplevel(window)
    filewin.geometry("300x300")
    button = Button(filewin, text="Do nothing button")
    button.pack()

def creamenu(window):
    menubar = Menu(window)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=lambda: donothing(window))
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