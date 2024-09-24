from sys import stdin
input = stdin.readline

n1 = input().strip()
n2 = input().strip()
n3 = input().strip()

k = 3
ans = 0
for i in [n1, n2, n3]:
	if i.isdigit():
		ans = int(i)
		break
	k -= 1

ans += k
if not ans % 3 and not ans % 5:
	print("FizzBuzz")
elif not ans % 3:
	print("Fizz")
elif not ans % 5:
	print("Buzz")
else:
	print(ans)