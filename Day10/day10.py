
def get_input():
    f = open("input.txt", "r")
    inp = f.read().split("\n")
    f.close()
    return inp

def remove_brackets(pos, str):
    l = str[pos]
    if pos>=len(str)-1:
        return str
    if l =="(" and str[pos + 1] == ")" or l == "[" and str[pos + 1] == "]" or l == "{" and str[pos + 1] == "}" or l == "<" and str[pos + 1] == ">"  :
        str = str[:pos] + str[pos + 2:]
        str = remove_brackets(0, str)
    else:
        str = remove_brackets(pos + 1, str)
    return str

def task1(inp):
    r = 0
    for i in inp:
        x = remove_brackets(0,i)
        for j in x:
            if j in ")]}>":
                if j == ")":
                    r+=3
                if j == "]":
                    r+=57
                if j == "}":
                    r+=1197
                if j == ">":
                    r+=25137
                break

    return r

def task2(inp):
    lst= [remove_brackets(0,i)for i in inp]
    lst = list(filter(lambda lst :not any([b in lst for b in [")","]","}",">"]]),lst))
    lst = [l[::-1] for l in lst]
    r = []
    for l in lst:
        tmp = 0
        ls = l.replace("(","1").replace("[","2").replace("{","3").replace("<","4")
        for x in ls:
            tmp=tmp*5+int(x)

        r.append(tmp)
    r.sort()
    return r[int(len(r)/2)]

def main():
    inp = get_input()
    print(f"Task 1: {task1(inp)}")
    print(f"Task 2: {task2(inp)}")

if __name__ == "__main__":
    main()