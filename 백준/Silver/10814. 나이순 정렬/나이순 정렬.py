import sys
input = sys.stdin.readline

n = int(input())
people = list()
for i in range(n):
	age, name = input().split()
	age = int(age)
	people.append((age, name))
people = sorted(people, key=lambda x:x[0])
for i in people:
	print(f'{i[0]} {i[1]}')