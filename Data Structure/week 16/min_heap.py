class MinHeap:
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
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    # Function to maintain heap property top-down after removal
    def heapify_down(self, index):
        n = len(self.heap)
        while index < n:
            smallest = index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

            if left_child < n and self.heap[left_child] < self.heap[smallest]:
                smallest = left_child
            if right_child < n and self.heap[right_child] < self.heap[smallest]:
                smallest = right_child

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
        
          # Function to remove and return the minimum element from the heap
    def remove_min(self):
        if not self.heap:
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapify_down(0)
        return min_val


# Example usage of MinHeap
min_heap = MinHeap()
arr = [3, 7, 1, 9, 2, 5]
min_heap.build_heap(arr)
print("Min Heap:", min_heap.heap)
min_heap.insert(4)
print("After Insertion:", min_heap.heap)
print("Removed Min:", min_heap.remove_min())
print("Min Heap after Removal:", min_heap.heap)
