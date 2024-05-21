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
    
    def is_circular(self):
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head.next

        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
    def is_circular(self):
        if self.head is None:
            return False
        slow = self.head
        fast = self.head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow=slow.next
            fast = fast.next.next
        return False

# Example usage:
sll = SinglyLinked()
sll.append(1)
sll.append(2)
sll.append(3)

# Uncomment the following line to make the linked list circular
# sll.head.next.next.next = sll.head

print("Is circular:", sll.is_circular())
