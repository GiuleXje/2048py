import func as f
import tkinter as tk
import random

generator = [2, 2, 2, 2, 4, 2, 2, 2, 2, 2] #random_choice(list) // import random


#modify the label of game matrix when making a move
def label_update(matrix, labels):
    for i, row in enumerate(labels):
        for j, update in enumerate(row):
            update.config(text=str(matrix[i][j]))
            if matrix[i][j] == 0:
                update.config(bg='snow')
            elif matrix[i][j] == 2:
                update.config(bg='yellow1')
            elif matrix[i][j] == 4:
                update.config(bg='green')
            elif matrix[i][j] == 8:
                update.config(bg='light salmon')
            elif matrix[i][j] == 16:
                update.config(bg='IndianRed4')
            elif matrix[i][j] == 32:
                update.config(bg='purple')
            elif matrix[i][j] == 64:
                update.config(bg='red1')
            elif matrix[i][j] == 128:
                update.config(bg='magenta')
            elif matrix[i][j] == 256:
                update.config(bg='DeepPink2')
            elif matrix[i][j] == 512:
                update.config(bg='cyan2')
            elif matrix[i][j] == 1024:
                update.config(bg='orange red')
            elif matrix[i][j] == 2048:
                update.config(bg='gold')


def set_labels(matrix, frame, labels):
    for i in range(0, 4):
        row = []
        for j in range(0, 4):
            label = tk.Label(frame, text=str(matrix[i][j]), borderwidth= 3, relief="solid",width= 7, height= 7, font=('Arial', 20))
            label.grid(row=i, column=j, sticky="nsew")
            row.append(label)
            if matrix[i][j] == 0:
                label.config(bg='white')
            elif matrix[i][j] == 2:
                label.config(bg='yellow')
            elif matrix[i][j] == 4:
                label.config(bg='green')
        labels.append(row)


def main(matrix, frame, window, score):
    labels = []
    set_labels(matrix, frame, labels)

    window.bind("<Left>", lambda event, matrix = matrix, score = score, labels = labels : f.move_LEFT(event, matrix, score, labels, window))
    window.bind("<Down>", lambda event, matrix = matrix, score = score, labels = labels : f.move_DOWN(event, matrix, score, labels, window))
    window.bind("<Up>", lambda event, matrix = matrix, score = score, labels = labels : f.move_UP(event, matrix, score, labels, window))
    window.bind("<Right>", lambda event, matrix = matrix, score = score, labels = labels : f.move_RIGHT(event, matrix, score, labels, window))


if __name__ == '__main__':
    main()