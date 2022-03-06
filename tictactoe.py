from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" TURN"))

            elif check_winner() is True:
                label.config(text=(players[0]+" WINS!"))

            elif check_winner() == "Tie":
                label.config(text="IT'S A TIE!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" TURN"))

            elif check_winner() is True:
                label.config(text=(players[1]+" WINS!"))

            elif check_winner() == "Tie":
                label.config(text="IT'S A TIE!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#703008")
            buttons[row][1].config(bg="#703008")
            buttons[row][2].config(bg="#703008")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#703008")
            buttons[1][column].config(bg="#703008")
            buttons[2][column].config(bg="#703008")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#703008")
        buttons[1][1].config(bg="#703008")
        buttons[2][2].config(bg="#703008")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#703008")
        buttons[1][1].config(bg="#703008")
        buttons[2][0].config(bg="#703008")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="#f03a3a")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" TURN")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Welcome to Tic-Tac-Toe Game")
#window['bg']='#f26913'
players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " TURN", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", bg='#f03a70',font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40),bg='#f26913', width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()

