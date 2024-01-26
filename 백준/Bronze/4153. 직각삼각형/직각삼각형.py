k, n ,m = map(int, input().split())
while k and n and m:
	if k*k + n*n == m*m:
		print("right")
	elif k*k + m*m == n*n:
		print("right")
	elif n*n + m*m == k*k:
		print("right")
	else:
		print("wrong")
	k, n ,m = map(int, input().split())