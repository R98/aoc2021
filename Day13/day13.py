import numpy as np
import re
def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n\n")
    inp = [i.split("\n") for i in inp]
    f.close()
    return inp
def fold(a,instruction):

    d = int(re.findall(r'\d+', instruction)[0])
    if "x" in instruction:
        a = a[0:d,]+np.flip(a[d+1:,],0)
    else:
        a = a[:,0:d] + np.flip(a[:,d + 1:], 1)
    a = np.where(a>0,1,0)
    return a

def task1(a,inst):
    a =fold(a, inst[0])
    return (a > 0).sum()

def task2(a,inst):
    print("Task 2: ")
    for i in inst:
        a = fold(a,i)
    a=a.transpose()
    for x in a:
        z = ""
        for y in x:
            z+=str(y)

        print(z.replace("0"," ").replace("1","#"))
    return

def main():
    inp = get_input()
    dots = [[int(x) for x in i.split(",")] for i in inp[0]]
    x = max(d[0] for d in dots)
    y = max(d[1] for d in dots)

    a = np.zeros((x + 1, y + 1), dtype=int)
    for dot in dots:
        a[dot[0], dot[1]] = 1
    print(f"Task 1: {task1(a,inp[1])}")
    task2(a,inp[1])
if __name__ == "__main__":
    main()