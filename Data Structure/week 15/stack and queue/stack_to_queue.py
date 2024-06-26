class StackToQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None  
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# Example usage:
queue = StackToQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
queue.enqueue(4)
print(queue.dequeue())  # Output: 3
print(queue.dequeue())  # Output: 4


