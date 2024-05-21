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
    
    def find_middle(self):
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow.data
    def find_middle(self):
        if self.head is None:
            return None
        slow = slow.head
        fast = fast.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
    def find_middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

# Example usage:
sll = SinglyLinked()
sll.append(1)
sll.append(2)
sll.append(6)
sll.append(4)
sll.append(5)
sll.append(5)

print( sll.find_middle())
