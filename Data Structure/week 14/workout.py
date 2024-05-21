
#singly ll 
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


#doubly ll

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
    