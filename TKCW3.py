from tkinter import*
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0),('paper',1),('scissors',2)]

def computer_wins():
    global computer_score ,player_score
    computer_score += 1
    winner_label.config(text = "Computer wins!")
    computer_score_label.config(text='Computer score:' + str(computer_score))
    player_score_label.config(text='player score:' + str(player_score))
    
def player_wins():
    global computer_score ,player_score
    player_score += 1
    winner_label.config(text = "player wins!")
    computer_score_label.config(text='Computer score:' + str(computer_score))
    player_score_label.config(text='player score:' + str(player_score))
    
def tie():
    global computer_score ,player_score
    computer_score += 1
    winner_label.config(text = "Tie!")
    computer_score_label.config(text='Computer score:' + str(computer_score))
    player_score_label.config(text='player score:' + str(player_score))
    
def player_choice(player_input):
    global player_score ,computer_score
    print(player_input)
    computer_input = get_computer_choice()
    print(computer_input)
    player_choice_label.config(text= 'You selcted'+ player_input[0])
    computer_choice_label.config(text= 'computer selcted'+ computer_input[0])
    
    if(player_input == computer_input):
        tie()
    
    #if the player chooses rock
    
    #nested loop
    if(player_input[1]==0):
        if(computer_input[1]==1):
            computer_wins()
        elif (computer_input[1]==2):
            player_wins()
            
    elif(player_input[1]==1):
        if(computer_input[1]==0):
            player_wins()
        elif (computer_input[1]==2):
            computer_wins()
            
    elif(player_input[1]==2):
        if(computer_input[1]==0):
            computer_wins()
        elif (computer_input[1]==1):
            player_wins()
            
def get_computer_choice():
    return random.choice(options)

game_window =Tk()
game_window.title("Rock Paper Scissors game!")

app_font = font.Font(size=12)
game_title = Label(text = "Rock paper scissors",font=font.Font(size=20),fg='grey')
game_title.pack()

winner_label = Label(text = "Lets start the game....",font=font.Font(size=13),fg='green',pady=8)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

player_options = Label(input_frame,text="Your options", font=app_font,fg='grey')    
player_options.grid(row = 0,column=0,pady=8)
  
rock_btn = Button(input_frame,text="Rock",width=15,bg='pink',pady=5,command = lambda: player_choice(options[0]))   
rock_btn.grid(row=1,column=1,padx=8,pady=5)

paper_btn = Button(input_frame,text="Paper",width=15,bg='silver',pady=5,command = lambda: player_choice(options[0]))   
paper_btn.grid(row=1,column=2,padx=8,pady=5)

scissors_btn = Button(input_frame,text="scisors",width=15,bg='light blue',pady=5,command = lambda: player_choice(options[0]))   
scissors_btn.grid(row=1,column=3,padx=8,pady=5)

score_label = Label(input_frame,text="score",font=app_font,fg='grey')   
score_label.grid(row=2,column=0,padx=8,pady=5)

player_choice_label = Label(input_frame,text="You selected:",font=app_font,fg='black')  
player_choice_label.grid(row=3,column=1,pady=5)

 
player_score_label = Label(input_frame,text="your score:",font=app_font)  
player_score_label.grid(row=3,column=2,pady=5)

computer_choice_label = Label(input_frame,text="computer selected:",font=app_font)  
computer_choice_label.grid(row=4,column=1,pady=5)

computer_score_label = Label(input_frame,text="Computer score:",font=app_font)  
computer_score_label.grid(row=4,column=2,pady=5,padx=(10,0))


 
game_window.geometry("700x300")
game_window.mainloop()
 
            
                  