from tkinter import *

def click(event):
    print(f'You have clicked on the button at {event.x} ,{event.y}')

root = Tk()
root.title("Evenets in Tkinter")
root.geometry("644x334")

widget = Button(root,text = "Click Here")
widget.pack()

widget.bind('<Button-1>',click)
widget.bind('<Double-1>',quit)

root.mainloop()
