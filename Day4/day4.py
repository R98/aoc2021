import re
import copy
import numpy as np

def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n\n")
    f.close()
    return inp
def sum_unmarked(board):
    s = 0
    for i in board:
        for j in i:
            if j != "x":
                s+=int(j)
    return s

def has_bingo(board):
    x = ["x","x","x","x","x"]
    for i in range(len(board)):
        if (board[i] == x).all():
            return sum_unmarked(board)
    board =np.transpose(board)
    for i in range(len(board)):
        if (board[i] == x).all():
            return sum_unmarked(board)
    return False
def task1(inp):
    numbers = inp[0].split(",")
    boards = []
    for i in range(1,len(inp)):
        x = re.findall(r'\d+',inp[i])
        board = np.array([x[0:5],x[5:10],x[10:15],x[15:20],x[20:25]])
        boards.append(board)
    for n in numbers:
        for i,b in enumerate(boards):
            if n in b:
                boards[i] = np.where(b == n, "x", b)
                x = has_bingo(boards[i])
                if x != False:
                    return x* int(n)

    return "no bingo"


def task2(inp):
    numbers = inp[0].split(",")
    boards = []
    for i in range(1, len(inp)):
        x = re.findall(r'\d+', inp[i])
        board = np.array([x[0:5], x[5:10], x[10:15], x[15:20], x[20:25]])
        boards.append(board)

    b2 = []
    for n in numbers:
        for i,b in enumerate(boards):
            if n in b:
                boards[i] = np.where(b == n, "x", b)
                x = has_bingo(boards[i])
                if x == False:
                    b2.append(boards[i])
            else:
                b2.append(boards[i])
        if len(b2)==0:
            return sum_unmarked(boards[0])*int(n)
        boards = b2
        b2 = []
    return "error"

def main():
    inp = get_input()
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")

if __name__ == "__main__":
    main()