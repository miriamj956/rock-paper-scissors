from tkinter import * 
import random
import tkinter.font as font

root = Tk()
root.geometry("700x300")

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def computer_wins():
    global player_score, computer_score
    computer_score +=1
    winnerLabel.config(text="Computer Wins!")
    Cscore.config(text = "Computer Score: " +str(computer_score))
    Pscore.config(text="Player Score: " +str(player_score))

def player_wins():
    global player_score, computer_score
    player_score +=1
    winnerLabel.config(text= "Player Wins!")
    Cscore.config(text="Computer Score: " +str(computer_score))
    Pscore.config(text="Player score: " +str(player_score))

def tie():
    global player_score, computer_score
    winnerLabel.config(text="Tie!")
    Cscore.config(text="Computer Score: " +str(computer_score))
    Pscore.config(text="Player score: " +str(player_score))

def get_computer_choice():
    return random.choice(options)

def get_player_choice(player_input):
    global player_score, computer_score
    print(player_input)
    computer_input = get_computer_choice()
    print(computer_input)
    Pselect.config(text='Your Selected: '+player_input[0])
    Cselect.config(text='Computer Selected: '+computer_input[0])
    if player_input == computer_input:
        tie()
    if(player_input[1] == 0):
        if(computer_input[1] == 1):
            computer_wins()
        elif(computer_input[1] == 2):
            player_wins()

    elif(player_input[1] == 1):
        if(computer_input[1] == 2):
            computer_wins()
        elif(computer_input[1] == 0):
            player_wins()

    elif(player_input[1] == 2):
        if(computer_input[1] == 0):
            computer_wins()
        elif(computer_input[1] == 1):
            player_wins()

label1 = Label(root, text="Rock, Paper, Scissors!")
label1.pack()

winnerLabel = Label(root, text="Start Game")
winnerLabel.pack()

frame1 = Frame(root)
frame1.pack()

app_font = font.Font(size=12)

player_options = Label(frame1, text= "Your Options: ", font=app_font, fg='grey')
player_options.grid(row=0, column=0, pady=8)

button1 = Button(frame1, text="Rock", bd=5, command= lambda: get_player_choice(options[0]))
button1.grid(row=1, column=1, pady = 5, padx = 10)

button2 = Button(frame1, text="Paper", bd=5, command= lambda: get_player_choice(options[1]))
button2.grid(row=1, column=2, pady = 5, padx = 10)

button3 = Button(frame1, text = "Scissors", bd = 5, command= lambda: get_player_choice(options[2]))
button3.grid(row=1, column=3, pady = 5, padx=10)

score = Label(frame1, text = "Score: ", font=app_font, fg='grey')
score.grid(row = 2, column=0, pady=10)

Pselect = Label(frame1, text="Your selection: ", pady=10)
Pselect.grid(row = 3, column=1)

Pscore =  Label(frame1, text="Your Score: ", pady=10)
Pscore.grid(row=3, column=2, padx=100)

Cselect = Label(frame1, text="Computer Selection: ", pady=10)
Cselect.grid(row=4, column=1)

Cscore = Label(frame1, text="Computer Score: ", pady = 10)
Cscore.grid(row=4, column=2)


root.mainloop()
