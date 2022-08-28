from tkinter import*
#because we are dealing with files we import filedialog
from tkinter.filedialog import*

master = Tk()
master.title("Memorizer")


def openFile():
    
    #akopenfile opens files on a computer which can be selcted
    fin = askopenfile(titile = "Open file")
    
    if fin is not NONE: #checks if the file we have selcted is not unknown
        listbox.delete(0, END)
        items = fin.readlines() #computer will read the selcted file
        for item in items:
            listbox.insert(END, item.strip())#strip removes the spaces in a file so it does not cause problems when copying

def saveFile():
    fout = asksaveasfile(defaultextension = ".txt") #all of the files that will be saved will be saves as txt file
    #ask saveasfile gives us the option to change or choose the name of a a file
    if fout is not NONE:
        for item in listbox.get(0,END):
            print(item.strip(),file=fout)
        listbox.delete(0,END)

def addItem():
    listbox.insert(END,item.get()) #when a new file is inserted, it will add it to the end of the list
    item.delete(0,END)

def deleteItem():
    index = listbox.curselection() #curselection is the paticular file the mouse selects
    if index:
        listbox.delete(index)
        
#create the buttons

fopen = Button(master,text = "OPEN", command = openFile,width = 15)
ldelete = Button(master,text ="DELETE",command = deleteItem, width = 15)
fsave = Button(master,text="SAVE",command = saveFile, width=15)

fopen.pack(side=LEFT,padx = 5,pady=5)
ldelete.pack(side=RIGHT,padx = 5,pady=5)
fsave.pack(padx = 5,pady=5)

LAdd = Button(master,text = "ADD",command=addItem,width=5)
item = Entry(master,width=35)
LAdd.pack(padx=5,pady=5)
item.pack(padx=5,pady=5)

frame = Frame(master)
scrollbar = Scrollbar(frame, orient = "vertical")

scrollbar.pack(side= RIGHT,fill = Y)
listbox = Listbox(frame,width=70,yscrollcommand = scrollbar.set,bg="light green")

for i in range(1,20):
    listbox.insert(END,"LIST"+str(i))

listbox.pack(side= LEFT,padx = 5)
scrollbar.config(command = listbox.yview)

frame.pack(side=RIGHT)
master.mainloop()