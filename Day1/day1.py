def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    f.close()
    for i in range(len(inp)):
        inp[i] = int(inp[i].strip())
    return inp

def task1(inp):
    counter = 0
    last = inp[0]
    for i in inp:
        if i > last:
            counter+=1
        last = i
    return counter

def task2(inp):
    counter = 0
    last = inp[0]+inp[1]+inp[2]
    for i in range(2,len(inp)):
        x = inp[i-2]+inp[i-1]+inp[i]
        if x > last:
            counter+=1
        last = x
    return counter

def day1(inp):
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")


def main():
    inp = get_input()
    day1(inp)

if __name__ == "__main__":
    main()