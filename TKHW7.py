
from tkinter import*
from tkinter.ttk import*

window = Tk()

window.title("Pizza App")

title = Label(window, text = "Welcome to Pizza Hut")
caption = Label(window, text = "Select your fav Pizza:")
caption2 = Label(window, text = "Enter quantity:")


title.grid(row=0,column=0,columnspan=3,pady=25)
caption.grid(row=1,column=0,padx=10)
caption2.grid(row=2,column=0, padx=10)

theflavours = StringVar()
flavours = Combobox(window,textvariable = theflavours,width = 13)

thequant = IntVar()
quantity = Combobox(window,textvariable=thequant,width=5)


flavours['values'] = ('Veg Extravganza', 'Pepperoni', 'Americano', 'Hawaiian', 'Pollo Americano', '5 cheese','Margarita')
quantity['values'] = tuple(range(10))

endVal = StringVar()
S = Radiobutton(window,text ="Small",variable = endVal,value="Small")
M = Radiobutton(window,text ="Medium",variable = endVal,value="Medium")
L = Radiobutton(window,text ="Large",variable = endVal,value="Large")


flavours.grid(column=1,row=1)
quantity.grid(column=1,row=2)
S.grid(column=2,row=1)
M.grid(column=2,row=2,padx=30)
L.grid(column=2,row=3,padx=30)


def generateTable():
    tables = ("You ordered "+ str(thequant.get()) + " " + (theflavours.get()) + " " +(endVal.get()) + " size pizza(s).")+"\n"
    table.configure(text=tables)
    
generateButton = Button(window,text="Generate table", command = generateTable)
table = Label(window,anchor="center")
generateButton.grid(row=4,column=1)
table.grid(row=5,column=1,pady=25)


window.mainloop()


