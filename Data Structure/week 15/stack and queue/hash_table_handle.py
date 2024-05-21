class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:  
                pair[1] = value
                return
        # Key doesn't exist, append new key-value pair 
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        print("not found")

    def delete(self, key):
        index = self._hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        print("Key not found")

# Example usage:
hash_table = HashTable(10)
hash_table.insert('apple', 5)
hash_table.insert('banana', 7)
hash_table.insert('cherry', 10)

print(hash_table.get('apple'))  # Output: 5
print(hash_table.get('banana'))  # Output: 7

# Inserting a key that results in a collision with 'apple'
hash_table.insert('lemon', 3)
print(hash_table.get('lemon'))  # Output: 3

hash_table.delete('banana')
hash_table.delete('bananas')
print(hash_table.get('banana'))