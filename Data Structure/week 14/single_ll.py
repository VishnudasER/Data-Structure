class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class SinglyLinked:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def Array_to_linked(self,arr):
        for i in arr:
            self.append(i)
            
    
arr=[43,54,34,234,35]
li =SinglyLinked()
li.Array_to_linked(arr)
li.print()


# li = SinglyLinked()
# li.append(43)
# li.append(2384)
# li.print()


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SinglyLinked:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def Array_to_linked(self,arr):
        for i in arr:
            self.append(i)
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
            
arr = [34,335,456,443,43]
arr=arr[::-1]
li=SinglyLinked()
li.Array_to_linked(arr)
li.print()


# li= SinglyLinked()
# li.append(6)
# li.append(763)
# li.append(2323)
# li.print()