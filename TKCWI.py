from tkinter import*

#import calendar module
import calendar

def showcal():
    new_gui = Tk() # creates window
    new_gui.config(background = "white") #background color
    new_gui.title("Calender") #title of window
    new_gui.geometry("550x600")  # size of the window
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)  #fetch calls the year and calendar
    cal_year = Label(new_gui, text=cal_content,font = "Consalas 10 bold")  #display something on the screen
    cal_year.grid(row = 5, column = 1, padx = 20)  
    new_gui.mainloop()        #starts everythign and initialises everything we have created

if __name__ == "__main__": #checks if the name is main file
    gui = Tk()
    gui.config(background='white')
    gui.title("Calendar")
    gui.geometry("250x140")
    cal = Label(gui,text="CALENDAR",bg="dark grey",font=("times", 28, 'bold'))
    year = Label(gui,text = "Enter the year",bg="light green")
    year_field = Entry(gui)
    Show = Button(gui,text = "Show calendar",fg = "black", bg="red", command=showcal) #fg = foreground bg= background
    exit = Button(gui,text = "Exit",fg = "black",bg="red",command=exit)

    #positoning and fomatting
    cal.grid(row=1,column=1)
    year.grid(row=2,column=1)
    year_field.grid(row=3,column=1)
    Show.grid(row=4,column=1)
    exit.grid(row=6,column=1)

    gui.mainloop()