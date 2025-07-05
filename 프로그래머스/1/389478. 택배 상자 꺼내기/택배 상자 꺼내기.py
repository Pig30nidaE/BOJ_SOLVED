def solution(n, w, num):
	h = n // w + 1
	boxes = [[0] * w for _ in range(h)]
	j = 0
	box_num = 1
	power = 1
	for i in range(h - 1, -1, -1):
		while 0 <= j < w:
			if box_num <= n:
				boxes[i][j] = box_num
				if box_num == num:
					answer = (i, j)
			j += power
			box_num += 1
		power *= -1
		j += power
	idx = 0
	while idx < answer[0] and not boxes[idx][answer[1]]:
		idx += 1
	answer = answer[0] - idx + 1
	return answer