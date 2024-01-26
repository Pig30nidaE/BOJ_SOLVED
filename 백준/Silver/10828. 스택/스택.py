class Stack:
	data = list()
	def push(self, num):
		self.data.append(num)
	def top(self):
		if len(self.data): print(self.data[-1])
		else: print("-1")
	def size(self):
		print(len(self.data))
	def empty(self):
		if len(self.data): print("0")
		else: print("1")
	def pop(self):
		if len(self.data): print(self.data.pop())
		else: print("-1")

if __name__ == '__main__':
	import sys
	input = sys.stdin.readline
	n = int(input())
	stack = Stack()
	for i in range(n):
		cmd = list(input().split())
		if len(cmd) > 1:
			eval(f"stack.{cmd[0]}({cmd[1]})")
		else:
			eval(f"stack.{cmd[0]}()")
		cmd.clear()