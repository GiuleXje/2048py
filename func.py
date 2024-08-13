import math
import sys
from game import label_update
import random
import time

#empty the matrix
def set_matrix(a):
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = 0

#check if the matrix is empty
def ungoing_game(a):
    if len(a) == 0:
        return False
    for i in range(0, 4):
        for j in range(0, 4):
            if a[i][j] != 0:
                return True
    return False

def generate_number(matrix):
    generator = [2, 2, 2, 2, 2, 4, 2, 2, 2, 2]
    positions = []
    k = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if matrix[i][j] == 0:
                positions.append(i * 4 + j)
                k = 1
    if k:
        pos = random.choice(positions)
        matrix[pos // 4][pos % 4] = random.choice(generator)
    del generator


#any possible move?
def check_for_moves(matrix):
    for i in range(0, 3):
        for j in range(0, 3):
            if matrix[i][j] == 0 or matrix[i][j] == matrix[i][j + 1] or matrix[i][j] == matrix[i + 1][j]:
                return True
    for i in range(0, 3):
        if matrix[i][3] == matrix[i + 1][3] or matrix[3][i] == matrix[3][i + 1] or matrix[i][3] == 0 or matrix[3][i] == 0:
            return True
    if matrix[3][3] == 0:
        return True
    return False

#can we go up?
def can_i_move_UP(matrix):
    for i in range(0, 3):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i + 1][j] and matrix[i][j]:
                return True
    for i in range(1, 4):
        for j in range(0, 4):
            if matrix[i][j] != 0 and matrix[i - 1][j] == 0:
                return True
    return False

#can we go down?
def can_i_move_DOWN(matrix):
    for i in range(0, 3):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i + 1][j] and matrix[i][j] != 0:
                return True
    for i in range(0, 3):
        for j in range(0, 4):
            if matrix[i][j] != 0 and matrix[i + 1][j] == 0:
                return True
    return False

#can we go right?
def can_i_move_RIGHT(matrix):
    for i in range(0, 4):
        for j in range(0, 3):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                return True
    for i in range(0, 4):
        for j in range(0, 3):
            if matrix[i][j] != 0 and matrix[i][j + 1] == 0:
                return True
    return False

#can we go left?
def can_i_move_LEFT(matrix):
    for i in range(0, 4):
        for j in range(0, 3):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                return True
    for i in range(0, 4):
        for j in range(1, 4):
            if matrix[i][j] != 0 and matrix[i][j - 1] == 0:
                return True
    return False

#the 4 following function will find out if any we
def check_line_rightwards(matrix, line, column):
    for i in range(column, 4):
        if matrix[line][i] != 0:
            return True
    return False

def check_column_downwards(matrix, column, line):
    for i in range(line, 4):
        if matrix[i][column] != 0:
            return True
    return False

def check_column_upwards(matrix, column, line):
    for i in range(line, -1, -1):
        if matrix[i][column] != 0:
            return True
    return False

def check_line_leftwards(matrix, line, column):
    for i in range(column, -1, -1):
        if matrix[line][i] != 0:
            return True
    return False

#close the window once the game is done
def end_game(window, matrix):
    if check_for_moves(matrix) == False:
        window.unbind_all("<Up>")
        window.unbind_all("<Left>")
        window.unbind_all("<Right>")
        window.unbind_all("<Down>")
        time.sleep(0.5)
        window.destroy()
        set_matrix(matrix)
        return True
    return False

def move_UP(event, matrix, score, labels, window):
    x = end_game(window, matrix)
    if x:
        return
    if can_i_move_UP(matrix) == False:
        return
    for i in range(0, 3):
        for j in range(0, 4):
            if check_column_downwards(matrix, j, i) == True:
                while matrix[i][j] == 0:
                    for k in range(i, 3):#nu e cea mai eficienta abordare
                        matrix[k][j] = matrix[k + 1][j]
                    matrix[3][j] = 0
    for i in range(0, 3):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i + 1][j] and matrix[i][j] != 0:
                matrix[i][j] = matrix[i][j] + matrix[i + 1][j]
                score[0] += matrix[i][j]
                for k in range(i + 1, 3):
                    matrix[k][j] = matrix[k + 1][j]
                matrix[3][j] = 0
    generate_number(matrix)
    label_update(matrix, labels)

def move_DOWN(event, matrix, score, labels, window):
    x = end_game(window, matrix)
    if x:
        return
    if can_i_move_DOWN(matrix) == False:
        return 
    for i in range(3, 0, -1):
        for j in range(3, -1, -1):
            if check_column_upwards(matrix, j, i) == True:
                while matrix[i][j] == 0:
                    for k in range(i, 0, -1):
                        matrix[k][j] = matrix[k - 1][j]
                    matrix[0][j] = 0
    for i in range(3, 0, -1):
        for j in range(0, 4):
            if matrix[i][j] == matrix[i - 1][j] and matrix[i][j] != 0:
                matrix[i][j] += matrix[i - 1][j]
                score[0] += matrix[i][j]
                for k in range(i - 1, 0, -1):
                    matrix[k][j] = matrix[k - 1][j]
                matrix[0][j] = 0
    generate_number(matrix)
    label_update(matrix, labels)

def move_RIGHT(event, matrix, score, labels, window):
    x = end_game(window, matrix)
    if x:
        return
    if can_i_move_RIGHT(matrix) == False:
        return 
    for j in range(3, 0, -1):
        for i in range(0, 4):
            if check_line_leftwards(matrix, i, j) == True:
                while matrix[i][j] == 0:
                    for k in range(j, 0, -1):
                        matrix[i][k] = matrix[i][k - 1]
                    matrix[i][0] = 0
    for j in range(3, 0, -1):
        for i in range (0, 4):
            if matrix[i][j] == matrix[i][j - 1] and matrix[i][j] != 0:
                matrix[i][j] += matrix[i][j - 1]
                score[0] += matrix[i][j]
                for k in range(j - 1, 0, -1):
                    matrix[i][k] = matrix[i][k - 1]
                matrix[i][0] = 0
    generate_number(matrix)
    label_update(matrix, labels)

def move_LEFT(event, matrix, score, labels, window):
    x = end_game(window, matrix)
    if x:
        return
    if can_i_move_LEFT(matrix) == False:
        return 
    for j in range(0, 3):
        for i in range(0, 4):
            if check_line_rightwards(matrix, i, j):
                while matrix[i][j] == 0:
                    for k in range(j, 3):
                        matrix[i][k] = matrix[i][k + 1]
                    matrix[i][3] = 0
    for j in range(0, 3):
        for i in range(0, 4):
            if matrix[i][j] == matrix[i][j + 1] and matrix[i][j] != 0:
                matrix[i][j] += matrix[i][j + 1]
                score[0] += matrix[i][j]
                for k in range(j + 1, 3):
                    matrix[i][k] = matrix[i][k + 1]
                matrix[i][3] = 0
    generate_number(matrix)
    label_update(matrix, labels)

