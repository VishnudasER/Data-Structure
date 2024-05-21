class MaxHeap:
    def __init__(self):
        self.heap = []

    # Function to heapify the array from the bottom-up
    def build_heap(self, arr):
        self.heap = arr
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(i)

    # Function to insert an element into the heap
    def insert(self, value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

 
    # Function to maintain heap property bottom-up after insertion
    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    # Function to maintain heap property top-down after removal
    def heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            largest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < n and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            if right_child < n and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break
       # Function to remove and return the maximum element from the heap
    def remove_max(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return max_val


# Example usage of MaxHeap
max_heap = MaxHeap()
arr = [3, 7, 1, 9, 2, 5]
max_heap.build_heap(arr)
print("Max Heap:", max_heap.heap)
max_heap.insert(10)
print("After Insertion:", max_heap.heap)
print("Removed Max:", max_heap.remove_max())
print("Max Heap after Removal:", max_heap.heap)
