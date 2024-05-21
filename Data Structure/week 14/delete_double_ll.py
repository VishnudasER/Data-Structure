class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
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
        
    def delete(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        
    def deletes(self,value):
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next      
                    
    
    def print(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    def Array_to_linked(self,arr):
        for i in arr:
            self.append(i)
            

arr= [234,465645,353,24,2]
arr = arr[::-1]
li=Double_linked()
li.Array_to_linked(arr)
li.deletes(2)
li.print()


class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.prev = None
        
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
            
            
    def delete(self,value):
        current= self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next= current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
            
