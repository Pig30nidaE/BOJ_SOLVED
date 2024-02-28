import sys
input = sys.stdin.readline


def postorderTraversal(tree:dict, node: str)->None:
	if tree[node][0] == '.' and tree[node][1] == '.':
		return print(node, end="")
	if tree[node][0] != '.': postorderTraversal(tree, tree[node][0])
	if tree[node][1] != '.': postorderTraversal(tree, tree[node][1])
	print(node, end="")

def inorderTraversal(tree: dict, node: str)->None:
	if tree[node][0] == '.' and tree[node][1] == '.':
		return print(node, end="")
	if tree[node][0] != '.': inorderTraversal(tree, tree[node][0])
	print(node, end="")
	if tree[node][1] != '.': inorderTraversal(tree, tree[node][1])

def preorderTraversal(tree: dict, node: str)->None:
	if node == '.': return
	print(node, end="")
	if tree[node][0] != '.': preorderTraversal(tree, tree[node][0])
	if tree[node][1] != '.': preorderTraversal(tree, tree[node][1])

n = int(input())
tree = dict()
for i in range(n):
	node, l_child, r_child = input().strip().split()
	tree[node] = [l_child, r_child]

preorderTraversal(tree, 'A');print()
inorderTraversal(tree, 'A'); print()
postorderTraversal(tree, 'A')