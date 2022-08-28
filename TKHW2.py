# build a currency converter from £ - $
#import tkinter
from tkinter import*

#create the window
mywin = Tk()
mywin.geometry("555x115")
mywin.config(background = "light blue")

#create the diffrent var for ecah currency

def from_pound():
    dollar = float(e2_value.get()) *1.3
    
    t1.delete("1.0",END) #writing starts from left to right
    t1.insert(END,dollar) #writing starts from right to left
    
e1 = Label(mywin,text="Pound(£) - dollar($) converter", bg = "light grey")
f1 = Label(mywin, text = "Source currency amount(£)", bg = "light grey")
e2_value = StringVar()
e2 = Entry(mywin,textvar=e2_value)
e3 = Label(mywin, text = "Target currency amount($)", bg = "light grey")


#create the buttons

t1 = Text(mywin,height=1,width=20)
but1 = Button(mywin,text = "Convert", command = from_pound)

e1.grid(row=0,column=1)
e2.grid(row=1,column=2)
f1.grid(row=1,column=0)
e3.grid(row=2,column=0)
t1.grid(row = 2, column =2)
but1.grid(row=3,column=1)

mywin.mainloop()

