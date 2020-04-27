from tkinter import *

root = Tk()

canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas Tutorial")
can_widget = Canvas(root,width = canvas_width,height = canvas_height)

can_widget.pack()

# The line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0 , fill= 'blue')

# to create a ract specify parameter in this order -
# coor of top left and coor of bootom right

can_widget.create_rectangle(3,5,700,300, fill = "blue")

can_widget.create_text(200,200, text= "Python")
#
# # This will come inside the rectange and
# # we will give the cor for inside of the rectangle
#
can_widget.create_oval(344,234,244,255)


root.mainloop()