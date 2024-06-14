import math
import sys
from game import label_update
import random
import time

#golim matricea
def set_matrix(a):
    for i in range(0, 4):
        for j in range(0, 4):
            a[i][j] = 0

#verificam daca matricea e goala
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


#verificam daca mai exista vreo mutare posibila
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

#verificam daca ne putem deplasa in sus
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

#verificam daca ne putem deplasa in jos
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

#verificam daca ne putem deplasa spre dreapta
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

#verificam daca ne putem deplasa spre stanga
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

#verificam daca pe linia i sunt numere diferite de 0, incepand cu coloana j, spre coloana 3
def check_line_rightwards(matrix, line, column):
    for i in range(column, 4):
        if matrix[line][i] != 0:
            return True
    return False

#verificam daca pe coloana j sunt numere diferite de 0, incepand cu linia i, spre linia 3
def check_column_downwards(matrix, column, line):
    for i in range(line, 4):
        if matrix[i][column] != 0:
            return True
    return False

#verificam daca pe coloana j sunt numere diferite de 0, incepand cu linia i, spre linia 0
def check_column_upwards(matrix, column, line):
    for i in range(line, -1, -1):
        if matrix[i][column] != 0:
            return True
    return False

#verifcam daca pe linia i sunt numere diferite de 0, incapand cu coloana j, spre coloana 0
def check_line_leftwards(matrix, line, column):
    for i in range(column, -1, -1):
        if matrix[line][i] != 0:
            return True
    return False

#inchidem fereasta cu jocul
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

#ne deplasam in sus
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

#ne deplasam in jos
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

#ne deplasam spre dreapta
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

#ne deplasam spre stanga
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

