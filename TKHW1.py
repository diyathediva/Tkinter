from tkinter import*

#create window
gamewin = Tk()
gamewin.config(background = "green")
gamewin.title("Minecraft")
gamewin.geometry("600x160")

def info():
    username = Label(gamewin, text = "Username : DiyaTheDiva123")
    age = Label(gamewin, text = "Age : 13")
    experience = Label(gamewin, text = "Experience : Professional")
    description = Label(gamewin, text = "Minecraft is the best!")

    age.grid(row = 1, column = 5)
    experience.grid(row = 2, column = 5)
    username.grid(row = 0, column = 5)
    description.grid(row = 3, column = 5)
    
def leaderboard():
    player1 = Label(gamewin, text = "1. Rambooisthebest12345!?")
    player2 = Label(gamewin, text = "2. Dream")
    player3 = Label(gamewin, text = "3. GeorgeNotFound98132")
    player4 = Label(gamewin, text = "4. Awesomegamerpro12345!!?!")
    
    player1.grid(row = 0, column = 5)
    player2.grid(row = 1, column = 5)
    player3.grid(row = 2, column = 5)
    player4.grid(row = 3, column = 5)
    

lab1 = Label(gamewin, text = "My Gamer Profile:",font=("times", 28, 'bold'))
lab2 = Label(gamewin, text = "Diyathediva123", font=(14))

lab1.grid(row=0,column=2)
lab2.grid(row=1,column=2)


button = Button(gamewin,text = "Info", command= info)
button1 = Button(gamewin,text = "Exit", command= exit)
button2 = Button(gamewin, text = "leaderboard", command=leaderboard)

button.grid(row = 3, column = 2)
button1.grid(row = 4, column = 2)
button2.grid(row=5,column=2)
gamewin.mainloop()