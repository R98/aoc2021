import re
import numpy as np
def get_input():
    f = open("input.txt", "r")
    inp = f.read()
    f.close()
    inp = [int(s) for s in re.findall(r'\d+',inp)]
    return inp

def task1(inp):

    inp.sort()
    median = inp[int(len(inp)/2)]

    r=sum([abs(median-crab) for crab in inp])
    return r

def task2(inp):
    avg = int(sum(inp)/len(inp))
    r = 0
    for i in inp:
        for j in range(0,abs(avg-i)):
            r+=j+1
    return r
def main():
    inp = get_input()
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")

if __name__ == "__main__":
    main()