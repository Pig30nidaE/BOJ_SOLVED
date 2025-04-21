from sys import stdin
from collections import deque
input = lambda : stdin.readline()

heap = deque()
realNum = dict()


def insert(num):
	abs_num = abs(num)
	if abs_num in realNum.keys():
		realNum[abs_num].append(num)
		realNum[abs_num].sort(reverse=True)
	else:
		realNum[abs_num] = [num]
	heap.append(abs_num)
	idx = len(heap) - 1
	if idx:
		parrent_idx = (idx - 1) // 2
	else:
		parrent_idx = 0
	while idx >= 0 and parrent_idx >= 0 and heap[idx] < heap[parrent_idx]:
		heap[idx], heap[parrent_idx] = heap[parrent_idx], heap[idx]
		idx = parrent_idx
		parrent_idx = (idx - 1) // 2

def remove():
	if heap:
		topop = heap.popleft()
		print(realNum[topop].pop())
	else:
		print(0)
		return
	idx = 0
	child1_idx = idx * 2 + 1
	child2_idx = idx * 2 + 2
	length = len(heap)
	if heap:
		heap.appendleft(heap.pop())
	while True:
		if child2_idx < length:
			if heap[idx] > heap[child2_idx]:
				if heap[idx] > heap[child1_idx]:
					min_idx = child1_idx if heap[child1_idx] < heap[child2_idx] else child2_idx
					heap[idx], heap[min_idx] = heap[min_idx], heap[idx]
					idx = min_idx
				else:
					heap[idx], heap[child2_idx] = heap[child2_idx], heap[idx]
					idx = child2_idx
			elif heap[idx] > heap[child1_idx]:
					heap[idx], heap[child1_idx] = heap[child1_idx], heap[idx]
					idx = child1_idx
			else:
				break
		elif child1_idx < length:
			if heap[idx] > heap[child1_idx]:
				heap[idx], heap[child1_idx] = heap[child1_idx], heap[idx]
				idx = child1_idx
			else:
				break
		else:
			break
		child1_idx = idx * 2 + 1
		child2_idx = idx * 2 + 2



def solution():
	n = int(input())
	for _ in range(n):
		op = int(input())
		if op:
			insert(op)
		else:
			remove()

if __name__ == '__main__':
	solution()
