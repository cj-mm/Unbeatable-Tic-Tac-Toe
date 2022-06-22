from tkinter import *
from functools import partial
from tkinter import messagebox
from minmax import *

NROW = 3
NCOL = 3

root = Tk()
root.title("Tic-Tac-Toe Game")

# start prompt
def start():
    prompt = Label(root, text="What do you want to play?")
    prompt.grid(row=0, column=0, columnspan=3, padx=10, pady=5)

    xBtn = Button(root, text="X", command=lambda: boardSetup("X"))
    xBtn.grid(row=1, column=0, padx=10, pady=10, ipadx=12, ipady=1)

    oBtn = Button(root, text="O", command=lambda: boardSetup("O"))
    oBtn.grid(row=1, column=1, padx=10, pady=10, ipadx=12, ipady=1)

    exitBtn = Button(root, text="EXIT", command=exitProgram)
    exitBtn.grid(row=1, column=2, padx=10, pady=10, ipadx=7, ipady=1)
    
    root.mainloop()

# exits the program
def exitProgram():
    exit()

# resets the board
def reset():
    widgets = root.winfo_children()
    for i in range(len(widgets)):
        widgets[i].destroy()

# set up (GUI). *board variable refers to the array representing the state of the game
def boardSetup(choice):
    firstTurn = True if choice == "X" else False
    board = [-1]*BOARDLEN

    for i in range(NROW):
        for j in range(NCOL):
            cell = Button(root, text="", width=3, padx=0, pady=10, font=('Helvetica', '75'), bg="black", activebackground="gray")
            cell.config(command=partial(move, choice, cell, board))
            cell.grid(row=i, column=j)
            if not firstTurn:
                cell.config(state=DISABLED)
                root.update()

    # if AI has the first turn, initialize the board with X (AI's move)
    if not firstTurn:
        cells = root.winfo_children()
        cells[4].config(text = "X")
        board[0] = 1

        for i in range(3, len(cells)):
            if cells[i]["text"] == "":
                cells[i].config(state=NORMAL)
            root.update()

# checks if the game is over
def checkGameOver(state, choice):
    result = checkState(state)
    if result != "not finished":
        if result == "draw":
            messagebox.showinfo("Game Over","Draw")
        elif result == 0:
            if choice == "O":
                messagebox.showinfo("Game Over","You Win!")
            else:
                messagebox.showinfo("Game Over","You Lose!")
        elif result == 1:
            if choice == "X":
                messagebox.showinfo("Game Over","You Win!")
            else:
                messagebox.showinfo("Game Over","You Lose!")
        reset()
        start()

# when a cell (not disabled) is clicked
def move(choice, cell, board):
    row = cell.grid_info()['row']
    col = cell.grid_info()['column']
    cells = root.winfo_children()
    board[row*NCOL+col] = 1 if choice == "X" else 0

    cell.config(text=choice)
    # disable the board first since it's the AI's turn
    for i in range(3, len(cells)): # start at index 3 to account the widgets from the prompt
        cells[i].config(state=DISABLED) 
        root.update()
    
    checkGameOver(board, choice)
    opponentsTurn(choice, board)

# AI's turn
def opponentsTurn(choice, board):
    cells = root.winfo_children()

    AIchoice = "O" if choice == "X" else "X"
    AImove = maxValue(board, AIchoice, choice)[0] # minmax algorithm, will return an array containing the action and its value

    cells[4+AImove].config(text = AIchoice)
    board[AImove] = 1 if AIchoice == "X" else 0

    checkGameOver(board, choice)

    # make the cells clickable again
    for i in range(3, len(cells)):
        if cells[i]["text"] == "":
            cells[i].config(state=NORMAL)
        root.update()