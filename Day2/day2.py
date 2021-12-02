import re

def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    f.close()
    return inp

def task1(inp):
    length = 0
    depth = 0
    for i in inp:
        x = int(re.findall(r'\d+',i)[0])
        if i.find("down")!=-1:
            depth+=x
        elif i.find("up")!=-1:
            depth-=x
        else:
            length+=x
    return depth*length

def task2(inp):
    length = 0
    depth = 0
    aim = 0
    for i in inp:
        x = int(re.findall(r'\d+', i)[0])
        if i.find("down") != -1:
            aim += x
        elif i.find("up") != -1:
            aim -= x
        else:
            length += x
            depth += x*aim
    return depth*length


def day1(inp):
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")


def main():
    inp = get_input()
    day1(inp)

if __name__ == "__main__":
    main()