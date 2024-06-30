scores = [6, 3, 2, 1, 2]
team1 = list(map(int, input().split()))
team2 = list(map(int, input().split()))

ans1 = 0
ans2 = 0
for i, j, k in zip(team1, team2, scores):
	ans1 += i * k
	ans2 += j * k
print(f'{ans1} {ans2}')