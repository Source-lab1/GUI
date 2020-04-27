from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value= eval(screen.get())
            except Exception as e:
                value = "Error"

        scvalue.set(value)
        screen.update()


    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("644x1000")
root.title("Calclator")
root.wm_iconbitmap("1.ico")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root,textvar = scvalue,font = "lucida 40 bold")
screen.pack(fill = X, ipadx = 8,padx = 10, pady = 5)

f_1 = Frame(root,bg="grey")
b_1 = Button(f_1,text="9",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_1.pack(side =LEFT ,padx = 5, pady = 1)
b_1.bind("<Button-1>",click)

b_2 = Button(f_1,text="8",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_2.pack(side = LEFT,padx = 5, pady = 1)
b_2.bind("<Button-1>",click)

b_3 = Button(f_1,text="7",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_3.pack(side = LEFT,padx = 5, pady = 1)
b_3.bind("<Button-1>",click)
f_1.pack()


f_1 = Frame(root,bg="grey")
b_1 = Button(f_1,text="6",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_1.pack(side =LEFT ,padx = 5, pady = 1)
b_1.bind("<Button-1>",click)

b_2 = Button(f_1,text="5",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_2.pack(side = LEFT,padx = 5, pady = 1)
b_2.bind("<Button-1>",click)

b_3 = Button(f_1,text="4",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_3.pack(side = LEFT,padx = 5, pady = 1)
b_3.bind("<Button-1>",click)
f_1.pack()


f_1 = Frame(root,bg="grey")
b_1 = Button(f_1,text="3",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_1.pack(side =LEFT ,padx = 5, pady = 1)
b_1.bind("<Button-1>",click)

b_2 = Button(f_1,text="2",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_2.pack(side = LEFT,padx = 5, pady = 1)
b_2.bind("<Button-1>",click)

b_3 = Button(f_1,text="1",padx = 28 ,pady = 5 ,font = "lucida 30 bold")
b_3.pack(side = LEFT,padx = 5, pady = 1)
b_3.bind("<Button-1>",click)
f_1.pack()

f_1 = Frame(root,bg="grey")
b_1 = Button(f_1,text="0",padx = 34 ,pady = 5 ,font = "lucida 25 bold")
b_1.pack(side =LEFT ,padx = 5, pady = 1)
b_1.bind("<Button-1>",click)

b_2 = Button(f_1,text="-",padx = 35 ,pady = 5 ,font = "lucida 26 bold")
b_2.pack(side = LEFT,padx = 5, pady = 1)
b_2.bind("<Button-1>",click)

b_3 = Button(f_1,text="*",padx = 34 ,pady = 5 ,font = "lucida 25 bold")
b_3.pack(side = LEFT,padx = 5, pady = 1)
b_3.bind("<Button-1>",click)
f_1.pack()

f_1 = Frame(root,bg="grey")
b_1 = Button(f_1,text="/",padx = 32 ,pady = 5 ,font = "lucida 26 bold")
b_1.pack(side =LEFT ,padx = 5, pady = 1)
b_1.bind("<Button-1>",click)

b_2 = Button(f_1,text="+",padx = 33 ,pady = 5 ,font = "lucida 26 bold")
b_2.pack(side = LEFT,padx = 5, pady = 1)
b_2.bind("<Button-1>",click)

b_3 = Button(f_1,text="=",padx = 32 ,pady = 5 ,font = "lucida 26 bold")
b_3.pack(side = LEFT,padx = 5, pady = 1)
b_3.bind("<Button-1>",click)
f_1.pack()

f_1 = Frame(root,bg="grey")
b_1 = Button(f_1,text="C",padx = 23 ,pady = 5 ,font = "lucida 30 bold")
b_1.pack(side =LEFT ,padx = 5, pady = 1)
b_1.bind("<Button-1>",click)

b_2 = Button(f_1,text="%",padx = 23 ,pady = 5 ,font = "lucida 30 bold")
b_2.pack(side = LEFT,padx = 5, pady = 1)
b_2.bind("<Button-1>",click)

b_3 = Button(f_1,text="**",padx = 23 ,pady = 5 ,font = "lucida 30 bold")
b_3.pack(side = LEFT,padx = 5, pady = 1)
b_3.bind("<Button-1>",click)
f_1.pack()


root.mainloop()


































