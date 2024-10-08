from sys import stdin
input = lambda: stdin.readline().strip()

class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DLList:
    def __init__(self):
        self.head = Node()
        self.curr = self.head

    def __iter__(self):
        v = self.head.next
        while v is not None:
            yield v.data
            v = v.next
    
    def insert(self, data):
        node = Node(data)
        node.prev = self.curr
        node.next = self.curr.next
        if node.next:
            node.next.prev = node
        self.curr.next = node
        self.curr = node

    def delete(self):
        if self.curr != self.head:
            self.curr.prev.next = self.curr.next
            if self.curr.next:
                self.curr.next.prev = self.curr.prev
            self.curr = self.curr.prev
    
    def move_prev(self):
        if self.curr != self.head:
            self.curr = self.curr.prev

    def move_next(self):
        if self.curr.next:
            self.curr = self.curr.next


t = int(input())
for _ in range(t):
    keyInput = input()
    dllist = DLList()
    for key in keyInput:
        if key == '<':
            dllist.move_prev()
        elif key == '>':
            dllist.move_next()
        elif key == '-':
            dllist.delete()
        else:
            dllist.insert(key)
    for data in dllist:
        print(data, end='')
    print()