from tkinter import *

root = Tk()

# Creating the Function for getting the values

def getvals():
    print('We have received your information ')


root.geometry("644x344")

# Heading

Label(root,text="Welcome to Nandesh Travels",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

# Text for our form
name = Label(root, text= 'Name')
phone = Label(root, text= 'Phone Number')
gender = Label(root, text= 'Gender')
emergency = Label(root, text= 'Emergency contact')
payment_mode = Label(root, text= 'Payment Mode')


# Pack Text for our form
name.grid(row=1, column =2)
phone.grid(row=2, column =2)
gender.grid(row=3, column =2)
emergency.grid(row=4, column =2)
payment_mode.grid(row=5, column =2)


# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root,textvariable = namevalue)
phoneentry = Entry(root,textvariable = phonevalue)
genderentry = Entry(root,textvariable = gendervalue)
emergencyentry = Entry(root,textvariable =emergencyvalue )
payment_modeentry = Entry(root,textvariable = paymentmodevalue)


#Packing the Entries for our form
nameentry.grid(row=1 , column=3)
phoneentry.grid(row=2 , column=3)
genderentry.grid(row= 3, column=3)
emergencyentry.grid(row= 4, column=3)
payment_modeentry.grid(row=5 , column=3)


# Checkbox & Packing it
foodservice = Checkbutton(text ="Want to prebook your meal ?",variable = foodservicevalue)
foodservice.grid(row = 6, column =3)

# Button & Packing it and asigning it a command
Button(text= "Submit To Nandesh Travels", command = getvals).grid(row=7,column=3)

root.mainloop()