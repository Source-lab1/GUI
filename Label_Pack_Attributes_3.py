
from tkinter import *
root = Tk()
root.geometry("744x133")
root.title("My GUI")
root.minsize(1100, 600)


# # Important Label Options
# # text - adds the text
# # bd - background
# # fg - foreground
# # font - sets the font
# # 1. font=("comicsansms", 19, "bold")
# # 2. font="comicsansms 19 bold"
#
# # padx - x padding
# # pady - y padding
# # relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
#
# title_label = Label(text="""As with most other modern Tk bindings,
#                          \n Tkinter is implemented as a Python wrapper around a complete Tcl interpreter
#                          \n embedded in the Python interpreter. \n Tkinter calls are translated into Tcl commands
#                          \n which are fed to this embedded interpreter, thus making it possible to mix Python
#                          \n and Tcl in a single application.""", bg = 'blue',  fg = 'black',
#                         padx= 35, pady = 55,font ="comicsense 19 bold ", borderwidth =3 ,
#                         relief = SUNKEN)
#
# # Important Pack options
# # anchor = nw
# # side = top, bottom, left, right
# # fill
# # padx
# # pady
#
# # title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
# title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)


root.mainloop()


