import numpy as np

r = c = 9
print("enter elements")
entries = list(map(int, input().split()))
sudoku = np.array(entries).reshape(r, c)
print(sudoku)

def possiblities(Row, Column, Num):
    global sudoku
    for i in range(0, 9):
        if sudoku[Row][i] == Num:
            return False
    
    for i in range(0, 9):
        if sudoku[i][Column] == Num:
            return False
    
    x = (Row // 3) * 3
    y = (Column // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[x + i][y + j] == Num:
                return False
    return True

def solution():
    global sudoku
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku[i][j] == 0:
                for num in range(1, 10):
                    if possiblities(i, j, num):
                        sudoku[i][j] = num
                        if solution():
                            return True
                        sudoku[i][j] = 0
                return False
    return True

print(np.matrix(sudoku))
print("Solving...")
print("more solutions")
solution()
print(np.matrix(sudoku))
