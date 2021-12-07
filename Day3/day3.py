import re
import numpy as np
def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    f.close()
    for i in range(len(inp)):
        inp[i] = inp[i].strip()
    return inp

def task1(inp):
    l = [0] * len(inp[0])
    for i in inp:
        l =np.add(l,[int(a) for a in str(i)])
    print(l)
    gamma = int("".join(["1" if int(i) > len(inp)/2 else "0" for i in l]),2)
    epsilon = pow(2,len(inp[0]))-1-gamma
    return gamma*epsilon


def task2(inp):
    length = len(inp[0])
    l = inp
    oxygen = 0
    co2=0
    for i in range(length):
        one = []
        zero = []
        for j in l:
            if str(j[i])=="1":
                one.append(j)
            else:
                zero.append(j)
        if len(one)>=len(zero):
            l = one
        else:
            l = zero
        if len(l)==1:
            oxygen = int(l[0],2)
    l = inp
    for i in range(length):
        one = []
        zero = []
        for j in l:
            if str(j[i])=="1":
                one.append(j)
            else:
                zero.append(j)
        if len(one)<len(zero):
            l = one
        else:
            l = zero
        if len(l)==1:
            co2 = int(l[0],2)

    return oxygen*co2

def main():
    inp = get_input()
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")

if __name__ == "__main__":
    main()