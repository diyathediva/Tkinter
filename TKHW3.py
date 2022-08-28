from time import time
from tkinter import*

mywin = Tk()
mywin.geometry("345x140")
mywin.title("Distance calculator!")

def calculates():
    distance = float(speed.get())*float(ti.get())
    
    t1.delete("1.0",END) 
    t1.insert(END,distance) 
    
value = StringVar
a1 = Label(mywin, text = "Enter the speed:",bg='light blue')
b1 = Label(mywin,text = "Enter time taken:",bg='pink')
speed = Entry(mywin,textvar=value)
ti = Entry(mywin,textvar=value)
c1= Label(mywin,text = "The distance of area:")

t1 = Text(mywin,height=1.5,width=25)
button1= Button(mywin,text="CALCULATE",bg='green',command=calculates)

a1.grid(row=1,column=0)
b1.grid(row=2,column=0)
speed.grid(row=1,column=1)
ti.grid(row=2,column=1)
c1.grid(row=7,column=0)
t1.grid(row=7,column=1)
button1.grid(row=4,column=1)
mywin.mainloop()