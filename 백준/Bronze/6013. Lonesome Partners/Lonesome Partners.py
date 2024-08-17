from sys import stdin
input = stdin.readline

n = int(input())
cors = list()
for _ in range(n):
	cors.append(tuple(map(int, input().split())))

cow1, cow2 = (0, 0), (0, 0)
max_distance = (cow1[0] - cow2[0]) ** 2 + (cow1[1] - cow2[1]) ** 2

for i in range(n):
	for j in range(i + 1, n):
		distance = (cors[i][0] - cors[j][0]) ** 2 + (cors[i][1] - cors[j][1]) ** 2
		if distance > max_distance:
			max_distance = distance
			cow1 = i
			cow2 = j

print(cow1 + 1, cow2 + 1)
