from sys import stdin
input = stdin.readline


n = int(input())
allCorrect = 0
info_dict = dict()
for i in range(n):
    info = list(input().strip().split())
    if info[1] == 'megalusion':
        continue
    else:
        if info[2] != '4':
            try:
                if not info_dict[info[1]][1]:
                    info_dict[info[1]][0] += 1
            except KeyError:
                info_dict[info[1]] = [1, False]
        else:
            try:
                if not info_dict[info[1]][1]:
                    allCorrect += 1
                info_dict[info[1]][1] = True
            except KeyError:
                allCorrect += 1
                info_dict[info[1]] = [0, True]
try:
    answer = f'{allCorrect / (allCorrect + sum(i[0] for i in info_dict.values() if i[1])) * 100:.10f}'
    print((allCorrect / (allCorrect + sum(i[0] for i in info_dict.values() if i[1]))) * 100)
except ZeroDivisionError:
    print(0)
        
