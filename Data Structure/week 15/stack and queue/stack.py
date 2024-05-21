class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)

print("Peek:", stack.peek())

print("Popped item:", stack.pop())
print("Peek:", stack.peek())
print("Stack after popping:", stack.items)

print("Size of stack:", stack.size())

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
     
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(34)
stack.push(44)
stack.push(87)
stack.push(545)
print(stack.items)
print(stack.pop())
print(stack.peek())
print(stack.peek())
print(stack.items)
print(stack.size())