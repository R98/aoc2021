import re
import numpy as np
def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    f.close()
    for i in range(len(inp)):
        inp[i] = [int(s) for s in re.findall(r'\d+',inp[i])]
    return inp

def task1(inp):
    arr = np.zeros((1000,1000))
    for i in inp:
        x1,y1,x2,y2 = i[0],i[1],i[2],i[3]
        if x1==x2:
            y = y1 if y1 <= y2 else y2
            for y in range(y,y+abs(y1 - y2)+1):
                arr[x1,y] +=1
        elif y1==y2:
            x = x1 if x1 <= x2 else x2
            for x in range(x,x+abs(x1 - x2)+1):
                arr[x,y1] +=1
    return (arr > 1).sum()

def task2(inp):
    arr = np.zeros((1000,1000))
    for i in inp:
        x1,y1,x2,y2 = i[0],i[1],i[2],i[3]
        if x1==x2:
            y = y1 if y1 <= y2 else y2
            for y in range(y,y+abs(y1 - y2)+1):
                arr[x1,y] +=1
        elif y1==y2:
            x = x1 if x1 <= x2 else x2
            for x in range(x,x+abs(x1 - x2)+1):
                arr[x,y1] +=1
        elif abs(x1-x2)==abs(y1-y2):
            if x1<=x2 and y1<=y2 or x1>=x2 and y1>=y2:# or y1<y2:
                x = x1 if x1 <= x2 else x2
                y = y1 if x == x1 else y2
                for j in range(0,abs(x1-x2)+1):
                    arr[x+j,y+j] +=1
            else:
                x = x1 if x1 >= x2 else x2
                y = y1 if x == x1 else y2
                for j in range(0,abs(x1-x2)+1):
                    arr[x-j,y+j] +=1

    return (arr > 1).sum()

def main():
    inp = get_input()
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")

if __name__ == "__main__":
    main()