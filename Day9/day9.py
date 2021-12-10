import re
import numpy as np
def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    f.close()
    inp = [[int(x) for x in re.findall(r'\d',s)] for s in inp]
    inp = np.array(inp).transpose()
    return inp

def task1(inp):
    lp = []
    inp = np.pad(inp, pad_width=1, mode='constant', constant_values=9)
    for x in range(1,len(inp)-1):
        for y,i in enumerate(inp[x][1:-1]):
            y+=1
            if inp[x,y-1]>i and inp[x,y+1]>i and inp[x-1,y]>i and inp[x+1,y]>i:
                lp.append(i)
    return sum(lp)+len(lp)

arr = []

def countbasin(x,y,r):
    global arr
    if arr[x,y]<9:
        r+=1
        arr[x,y]=9
        if arr[x-1,y]<9:
            r = countbasin(x-1,y,r)
        if arr[x+1,y]<9:
            r = countbasin(x+1,y,r)
        if arr[x,y-1]<9:
            r = countbasin(x,y-1,r)
        if arr[x,y+1]<9:
            r = countbasin(x,y+1,r)
        return r
    else:
        return r

def task2(inp):
    inp = np.pad(inp, pad_width=1, mode='constant', constant_values=9)
    inp = np.where(inp<9,0,inp)
    global arr
    arr = inp
    r = []
    for x in range(1,len(inp)-1):
        for y in range(len(inp[x][1:-1])):
            r.append(countbasin(x,y,0))
    r.sort(reverse=True)
    return r[0]*r[1]*r[2]

def main():
    inp = get_input()
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")

if __name__ == "__main__":
    main()