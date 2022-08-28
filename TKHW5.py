from tkinter import*
import tkinter.messagebox
import random

root = tkinter.Tk()
root.minsize(345,160)
root.title('Guess the Product!')
root.config(background = 'light green')

num1 = (random.randint(1,12))
num2 = (random.randint(1,12))

def product_check():
    productguess = text_guess.get()
    productguess = int(productguess)
    
    if productguess > int(num1*num2):
        tkinter.messagebox.showinfo("High","Your guess is too high!")
    if productguess < int(num1*num2):
        tkinter.messagebox.showinfo("Low","Your guess is too low!")
    if productguess == int(num1*num2):
        tkinter.messagebox.showinfo("Correct","Good job! ")
        root.quit()


def btn_confirm():
    tkinter.messagebox.showinfo("number",'I am thinking of a number between 1 and 12 that will multiply with the number ' + str(num2) + ' to get my mystery product. Can you guess my product?')
    


label = tkinter.Label(root,text='Welcome to the game', font= 'Consolas 14 bold')
label.pack()



btnok = tkinter.Button(root,text="CLICK HERE TO PLAY", font = 'Comic 10 bold', fg = "green", command=btn_confirm)
btnok.place(x=90,y=30,height=28)

label_guess = tkinter.Label(root,text='Your guess:', fg='green', font = 'Comic 12 bold')
label_guess.place(x=10,y=90)

text_guess = tkinter.Entry(root,width=10)
text_guess.place(x=90,y=90)

btncheck = tkinter.Button(root,text='Guess', font= 'Comic 10 bold',command=product_check)
btncheck.place(x=200,y=90,width=45,height=28)

root.mainloop()