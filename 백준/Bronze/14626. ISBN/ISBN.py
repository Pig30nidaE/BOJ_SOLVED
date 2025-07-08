ISBN = input()
flag = True
ans = 0
for i in ISBN:
    if i != '*':
        if flag:
            ans += int(i)
        else:
            ans += 3 * int(i)
    else:
        ans_flag = flag
    flag = not flag
count = 0
while (ans + count) % 10:
    if ans_flag:
        count += 1
    else:
        count += 3
if ans_flag:
    print(count)
else:
    print(count // 3)