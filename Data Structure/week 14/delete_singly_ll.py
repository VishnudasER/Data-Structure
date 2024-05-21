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
        
    def delete(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        prev_node = self.head
        current = self.head.next
        while current and current.data != value:
            prev_node, current = current, current.next
        if current:
            prev_node.next = current.next
    
    def deleted(self,value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        prev_node = self.head
        current = self.head.next
        while current and current.data != value:
            prev_node, current = current, current.next
        if current:
            prev_node.next = current.next
            
        
        
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def Array_to_linked(self,arr):
        for i in arr:
            self.append(i)
            
    
arr=[43,54,34,234,35,45]
li =SinglyLinked()
li.Array_to_linked(arr)
li.delete(35)
li.deleted(45)
li.print()


# li = SinglyLinked()
# li.append(43)
# li.append(2384)
# li.print()
