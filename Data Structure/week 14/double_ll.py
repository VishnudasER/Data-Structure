class Node:
    def __init__(self,data):
        self.data =data
        self.prev = None
        self.next = None
        
class Double_linked:
    def __init__(self):
        self.head = None
        
    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node=self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node
    
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
 
dll = Double_linked()
dll.append(1)
dll.append(2)
dll.append(3)
dll.print()

class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
class Double_linked:
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
        new_node.prev = last_node
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    
           

dll = Double_linked()
dll.append(1)
dll.append(2)
dll.append(3)
dll.print()