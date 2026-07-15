import customtkinter as ctk
from tkinter import messagebox

# ---------------- Appearance ---------------- #

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Sudoku Solver")
app.geometry("850x750")
app.resizable(False, False)

# ---------------- Sudoku Algorithm ---------------- #

board = [[0 for _ in range(9)] for _ in range(9)]

def is_valid(board, row, col, num):

    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3

    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True


def solve(board):

    for row in range(9):

        for col in range(9):

            if board[row][col] == 0:

                for num in range(1,10):

                    if is_valid(board,row,col,num):

                        board[row][col]=num

                        if solve(board):
                            return True

                        board[row][col]=0

                return False

    return True

# ---------------- Functions ---------------- #

entries=[]

def read_board():

    for i in range(9):
        for j in range(9):

            value=entries[i][j].get()

            if value=="":

                board[i][j]=0

            else:

                try:
                    num=int(value)

                    if num<1 or num>9:
                        raise ValueError

                    board[i][j]=num

                except:
                    messagebox.showerror("Invalid","Enter numbers 1-9 only")
                    return False

    return True


def show_board():

    for i in range(9):
        for j in range(9):

            entries[i][j].delete(0,"end")

            if board[i][j]!=0:

                entries[i][j].insert(0,str(board[i][j]))


def solve_board():

    if not read_board():
        return

    if solve(board):

        show_board()

        status.configure(
            text="✅ Sudoku Solved Successfully!",
            text_color="lightgreen"
        )

    else:

        messagebox.showerror("No Solution","This puzzle has no solution.")


def clear_board():

    global board

    board=[[0 for _ in range(9)] for _ in range(9)]

    for row in entries:
        for cell in row:
            cell.delete(0,"end")

    status.configure(
        text="Board Cleared",
        text_color="white"
    )


def sample_board():

    sample = [

        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]

    ]

    for i in range(9):
        for j in range(9):

            entries[i][j].delete(0,"end")

            if sample[i][j]!=0:
                entries[i][j].insert(0,str(sample[i][j]))

    status.configure(
        text="Sample Puzzle Loaded",
        text_color="cyan"
    )

# ---------------- UI ---------------- #

title=ctk.CTkLabel(
    app,
    text="🧩 Sudoku Solver",
    font=("Segoe UI",34,"bold")
)

title.pack(pady=20)

frame=ctk.CTkFrame(app,corner_radius=20)

frame.pack(pady=10)

for i in range(9):

    row=[]

    for j in range(9):

        cell=ctk.CTkEntry(
            frame,
            width=45,
            height=45,
            justify="center",
            font=("Arial",20)
        )

        cell.grid(
            row=i,
            column=j,
            padx=3,
            pady=3
        )

        row.append(cell)

    entries.append(row)

button_frame=ctk.CTkFrame(app)

button_frame.pack(pady=25)

solve_btn=ctk.CTkButton(
    button_frame,
    text="Solve Sudoku",
    width=180,
    height=45,
    command=solve_board
)

solve_btn.grid(row=0,column=0,padx=15)

sample_btn=ctk.CTkButton(
    button_frame,
    text="Load Sample",
    width=180,
    height=45,
    fg_color="orange",
    hover_color="#b36b00",
    command=sample_board
)

sample_btn.grid(row=0,column=1,padx=15)

clear_btn=ctk.CTkButton(
    button_frame,
    text="Clear Board",
    width=180,
    height=45,
    fg_color="red",
    hover_color="darkred",
    command=clear_board
)

clear_btn.grid(row=0,column=2,padx=15)

status=ctk.CTkLabel(
    app,
    text="Enter Sudoku Puzzle",
    font=("Segoe UI",18)
)

status.pack(pady=20)


app.mainloop()