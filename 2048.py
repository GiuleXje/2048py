import tkinter as tk
from tkinter import *
import func as f
import game
import random

#leaderboard's top 10
top10 = []

#the list that will help insert a new number in the game matrix
generator = [2, 2, 2, 2, 4, 2, 2, 2, 2, 2] #random.choice(list) // import random


#folosim event deoarece atunci cand dorim sa trecem la urmatoarea fereastra
#apasand enter functia noastra primeste ca parametru tasta enter
#iar fara event am avea urmatoare eroare:
#Game_main_window() takes 0 positional arguments but 1 was given
def Game_main_window(event, user_window, matrix, score):
    user_window.destroy()

    window = tk.Tk()
    window.configure(bg='black')
    window.title('2048.exe')
    window.geometry('1920x1080')
    #window.configure(bg='grey')

    #creating a frame for the matrix
    frame = tk.Frame(window)
    frame.configure(bg= 'white')
    #nsew (north, south, east, west), the frame sticks to all sides of the cell
    #frame.grid(row=0, column=0, sticky= "nsew")

    #center the frame
    frame.place(relx=0.5, rely=0.5, anchor='center')

    game.main(matrix, frame, window, score)

    window.mainloop()


'''def Game(name):
    print(name.get())
    username = name.get()
    # messagebox.showinfo('Logged in', username + ' logged in succesfully')
    Game_main_window()'''


#creating a window where you can type in your username
def type_username(matrix, score):
    user_window = tk.Tk()
    user_window.geometry('1920x1080')
    user_window.title("")

    Label(user_window, text='Username: ').grid(row=0, column=0)

    name = Entry(user_window)
    name.grid(row=0, column=1)
    #setting the keyboard focus on the username grid
    name.focus_set()

    #SAU(plus altele)
    #L1 = Label(user_window, text='')
    #L1.pack(side='left')
    #E1 = Entry(top, bd= 5)
    #E1.pack(side='right')

    #lambda delays the execution of the Game function until you click the 'Start game' button
    #button = Button(user_window, text='Start game', command=lambda : Game(name)).grid(row=1, column=0,columnspan=2)
    #i would use this if i would want a button that sends me to the Game window

    #the event is the moment i press the 'Enter' key and var is the username window in which
    #i type in the username and i pass it as an argument because i want to close this window once i start the game
    #"<Return>" is 'Enter' key
    name.bind("<Return>", lambda event, var=user_window, matrix = matrix: Game_main_window(event, var, matrix, score))

    user_window.mainloop()

def new_game(matrix, score):
    print("Started a new game")
    matrix = []
    for i in range(0, 4):
        matrix.append([0, 0, 0, 0])
        for j in range(0, 4):
            matrix[i][j] = int(matrix[i][j])
    position_generator = list(range(16))
    pos1 = random.choice(position_generator)
    position_generator.remove(pos1)
    pos2 = random.choice(position_generator)
    del position_generator
    matrix[pos1 // 4][pos1 % 4] = random.choice(generator)
    matrix[pos2 // 4][pos2 % 4] = random.choice(generator)

    type_username(matrix, score)


def resume_game(matrix, score):
    if f.ungoing_game(matrix) == False:
        print("No game ungoing! Staring a new one...")
        new_game(matrix, score)
        return
    print("Game resumed")


def show_leaderboard(a):
    a.destroy()

    print("Showing leaderboard...")
    window = tk.Tk()

    window.title("Leaderboard")

    window.geometry('600x500')

    window.mainloop()

    main()


def main():

    #game matrix and it's initialization
    matrix = []
    score = [0]

    #create a tkinter window
    window = tk.Tk()

    #set up the window title
    window.title("2048.exe")

    #set the window size
    window.geometry("1920x1080")

    #set window colour
    window.configure(bg='black')


    #create a label / titlu
    label = tk.Label(window, text='Pick an option', height=3, width=20, font=('Arial', 28))
    label.configure(bg='black',fg='#00F5FF')#changing the label background colour
    label.pack()

    #create a button
    button1 = tk.Button(window, text='Resume', command= lambda : resume_game(matrix, score), height=6, width=20, font=('Arial', 15))
    button1.configure(bg='#C71585')
    button1.place(relx=.5, rely=.4, anchor='center')
    #button1.pack()

    button2 = tk.Button(window, text='New game', command= lambda : new_game(matrix, score), height=6, width=20, font=('Arial', 15))
    button2.configure(bg='#00C957')
    button2.place(relx=.5, rely=.5, anchor='center')
    #button2.pack()

    button3 = tk.Button(window, text='Leaderboard', command=lambda : show_leaderboard(window), height=6, width=20, font=('Arial', 15))
    button3.configure(bg='#FFFF00')
    button3.place(relx=.5, rely=.6, anchor='center')
    #button3.pack()
    #we would use pack when we don't want to place the buttons on a specific place

    #start the main event loop
    window.mainloop()
    del matrix

if __name__ == '__main__':
    main()