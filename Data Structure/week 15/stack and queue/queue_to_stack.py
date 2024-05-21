class QueueToStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, item):
        self.queue1.append(item)

    def pop(self):
        if not self.queue1:
            return None  # Stack is empty
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop(0)

# Example usage:
stack = QueueToStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
stack.push(4)
print(stack.pop())  # Output: 4
print(stack.pop())  # Output: 1

class QueuetoStack:
    def __init__(self):
        self.queue1 =[]
        self.queue2 = []
    def push(self,item):
        self.queue1.appennd(item)
    def pop(self):
        if not self.queue1:
            return None
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))
        self.queue1,self.queue2 = self.queue2,self.queue1
        return self.queue2.pop(0)

class Stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) ==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        

def reverse_string(string):
    stack = Stack()
    string=string.lower()
    reversed = ""
    for i in string:
        stack.push(i)
    while not stack.is_empty():
        reversed+=stack.pop()
    return reversed

string = "Hi iam"
string= reverse_string(string)
print(string)
         