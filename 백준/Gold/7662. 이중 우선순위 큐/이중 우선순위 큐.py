from sys import stdin, stdout
from queue import PriorityQueue
input = stdin.readline
print = stdout.write


def solution():
	t = int(input())
	for _ in range(t):
		k = int(input())
		max_queue = PriorityQueue()
		min_queue = PriorityQueue()
		real_num = dict()
		for i in range(k):
			cmd, num = input().strip().split()
			num = int(num)
			if cmd == 'I':
				max_queue.put(-num)
				min_queue.put(num)
				if num in real_num.keys():
					real_num[num] += 1
				else:
					real_num[num] = 1
			else:
				if num > 0:
					while max_queue.queue:
						num = -max_queue.get(block=False)
						if real_num[num] > 0:
							real_num[num] -= 1
							break
				else:
					while min_queue.queue:
						num = min_queue.get(block=False)
						if real_num[num] > 0:
							real_num[num] -= 1
							break
		toPrint = []
		for key, value in real_num.items():
			if value:
				toPrint.append(key)
		toPrint.sort()
		if toPrint:
			print(f'{toPrint[-1]} {toPrint[0]}\n')
		else:
			print('EMPTY\n')


if __name__ == '__main__':
	solution()