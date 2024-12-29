from sys import stdin, stdout
from collections import deque
input = lambda : int(stdin.readline())

if __name__ == '__main__':
    n = int(input())

    max_heap = deque()
    answer_list = []
    for _ in range(n):
        command = input()
        if command == 0:
            if max_heap:
                answer_list.append(max_heap.popleft())
                max_heap.rotate(1)
                idx = 0
                child1 = idx * 2 + 1
                child2 = idx * 2 + 2
                while child1 < len(max_heap) or child2 < len(max_heap):
                    if child1 < len(max_heap) and child2 < len(max_heap):
                        if max_heap[child1] < max_heap[child2]:
                            if max_heap[idx] < max_heap[child2]:
                                max_heap[idx], max_heap[child2] = max_heap[child2], max_heap[idx]
                                idx = child2
                            else:
                                break
                        else:
                            if max_heap[idx] < max_heap[child1]:
                                max_heap[idx], max_heap[child1] = max_heap[child1], max_heap[idx]
                                idx = child1
                            else:
                                break
                    elif child1 < len(max_heap):
                        if max_heap[child1] > max_heap[idx]:
                            max_heap[idx], max_heap[child1] = max_heap[child1], max_heap[idx]
                            idx = child1
                        else:
                            break
                    elif child2 < len(max_heap):
                        if max_heap[child2] > max_heap[idx]:
                            max_heap[idx], max_heap[child2] = max_heap[child2], max_heap[idx]
                            idx = child2
                        else:
                            break
                    child1 = idx * 2 + 1
                    child2 = idx * 2 + 2
            else:
                answer_list.append(0)
        else:
            max_heap.append(command)
            idx = len(max_heap) - 1
            parrent = (idx - 1) // 2
            while parrent >= 0 and idx >= 0 and idx != parrent and max_heap[parrent] < max_heap[idx]:
                max_heap[idx], max_heap[parrent] = max_heap[parrent], max_heap[idx]
                idx = parrent
                parrent = (idx - 1) // 2
    for s in answer_list:
        stdout.write(str(s))
        stdout.write("\n")
        

