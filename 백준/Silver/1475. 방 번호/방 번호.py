n = input()
numberSet = [0 for i in range(10)]

flag = False
for i in n:
    if i == '6' or i == '9':
        if not flag:
            numberSet[6] += 1
            flag = True
        else:
            numberSet[9] += 1
            flag = False
    else:
        numberSet[int(i)] += 1
print(max(numberSet))