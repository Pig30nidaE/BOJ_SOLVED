from sys import stdin
input = lambda : stdin.readline().strip()


def split_(formula: str):
    return_arr = []
    num = ''
    for s in formula:
        if s == '+' or s== '-':
            return_arr.append(int(num))
            num = ''
            return_arr.append(s)
        else:
            num += s
    return_arr.append(int(num))
    return return_arr
    
if __name__ == '__main__':
    formula = input()
    split_list = split_(formula)
    stack = []
    res = 0
    for i in range(len(split_list) - 1, -1, -1):
        if isinstance(split_list[i], int):
            stack.append(split_list[i])
        else:
            if split_list[i] == '-':
                while stack:
                    res -= stack.pop()
    while stack:
        res += stack.pop()
    print(res)