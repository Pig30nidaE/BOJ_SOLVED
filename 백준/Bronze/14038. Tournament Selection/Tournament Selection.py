win_count = 0
for _ in range(6):
	if input() == 'W': win_count += 1
if win_count in  (5, 6): print(1)
elif win_count in (3, 4): print(2)
elif win_count in (1, 2): print(3)
else: print(-1)
