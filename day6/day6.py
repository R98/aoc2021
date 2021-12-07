import re
import numpy as np
def get_input():
    f = open("input.txt", "r")
    inp = f.read()
    f.close()
    inp = [int(s) for s in re.findall(r'\d+',inp)]
    return inp

def lanternfish(inp,days):
    fish = [0]*9
    for i in inp:
        fish[i] +=1
    for i in range(days):
        x = fish.pop(0)
        fish.append(x)
        fish[6]+=x
    return sum(fish)

def main():
    inp = get_input()
    print(f"Task 1: {lanternfish(inp,80)}")
    print(f"Task 2: {lanternfish(inp,256)}")

if __name__ == "__main__":
    main()