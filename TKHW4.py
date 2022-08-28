from tkinter import*
from tkinter.ttk import*
import time

from time import strftime
from turtle import delay

root = Tk()
root.title("Clock")
root.geometry('300x110')

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000,time)
   
lbl = Label(root, font=('comic', 40),)
lbl.pack(anchor='center')


def get_colour():
    list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'violet']
    while True:
        for c in list:
            yield c
def start():
    root.config(background=next(get)) # set the colour to the next colour generated
    root.after(1000, start) # run this function again after 1000ms

get = get_colour()
btn = Button(root,text="START COLOURS",command=start)
btn.pack()

lbl2 = Label(root,text="My Digital clock")
lbl2.pack()
    

time()

mainloop()
    