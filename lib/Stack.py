# lib/stack.py
class Stack:
    def __init__(self, items=[], limit=100):
        self.items = items
        self.limit = limit

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise IndexError("push to full stack")

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        try:
            index = len(self.items) - self.items[::-1].index(target) - 1
            return len(self.items) - 1 - index
        except ValueError:
            return -1
