# class Stack:

#     def __init__(self, items = None, limit = 100):
#         pass
#     def isEmpty(self):
#         pass

#     def push(self, item):
#         pass

#     def pop(self):
#         pass

#     def peek(self):
#         pass
    
#     def size(self):
#         pass

#     def full(self):
#         pass

#     def search(self, target):
#         pass



class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        if target in self.items:
            return self.items.index(target)
        else:
            return -1
