class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
       
    def peek(self):
        if not self.is_empty():
            return self.items[0]
       

    def size(self):
        return len(self.items)

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print("Queue:", queue.items)

print("Peek:", queue.peek())

print("Dequeued item:", queue.dequeue())
print("Queue after dequeuing:", queue.items)

print("Size of queue:", queue.size())

class Que:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
    def size(self):
        return len(self.items)
    
queue=Que()
queue.enqueue(43)
queue.enqueue(12)
queue.enqueue(67)
queue.enqueue(65)
print(queue.items)
print(queue.dequeue())
print(queue.dequeue())
print(queue.peek())
print(queue.items)
print(queue.size())

class StacktoQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def enqueue(self,item):
        self.stack1.append(item)
    
    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        
s=StacktoQueue()
s.enqueue(78)
s.enqueue(12)
print(s.dequeue())        

class QueueToStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 =[]
    
    def push(self,item):
        self.queue1.append(item)
    
    def pop(self):
        if not self.queue1:
            return None
        while len(self.queue1) >=0:
            self.queue2.append(self.queue1.pop())
        self.queue1,self.queue2=self.queue2,self.queue1
        return self.queue2.pop()
     