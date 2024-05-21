# class HashTable:
#     def __init__(self, size):
#         self.size = size
#         self.table = [[] for _ in range(size)]

#     def _hash_function(self, key):
#         return hash(key) % self.size

#     def insert(self, key, value):
#         index = self._hash_function(key)
#         self.table[index].append((key, value))

#     def get(self, key):
#         index = self._hash_function(key)
#         for k, v in self.table[index]:
#             if k == key:
#                 return v
#         print("key not found")

#     def delete(self, key):
#         index = self._hash_function(key)
#         for i, (k, v) in enumerate(self.table[index]):
#             if k == key:
#                 del self.table[index][i]
#                 return
#         print("key not found")


# # Example usage:
# hash_table = HashTable(10)
# hash_table.insert('apple', 5)
# hash_table.insert('banana', 7)
# hash_table.insert('cherry', 10)

# print(hash_table.get('apple'))  # Output: 5
# print(hash_table.get('banana'))  # Output: 7

# hash_table.delete('banana')
# print(hash_table.get('banana'))  # Raises KeyError: 'Key 'banana' not found'

# class HashTable:
#     def __init__(self,size):
#         self.size = size
#         self.table = [[] for _ in range(size)]
        
#     def _hash_function(self,key):
#         return hash(key) % self.size
    
#     def insert(self,key,value):
#         index = self._hash_function(key)
#         self.table[index].append((key,value))
        
#     def get(self,key):
#         index = self._hash_function(key)
#         for k,v in self.table[index]:
#             if k == key:
#                 return v
#             else:
#                 print("Not Found")
                
#     def delete(self,key):
#         index = self._hash_function(key)
#         for i,(k,v) in enumerate(self.table[index]):
#             if k == key:
#                 del self.table[index][i]
#                 return
#         print("Key not Found")
        
# # Example usage
# hash_table = HashTable(5)

# # Inserting key-value pairs
# hash_table.insert("apple", 10)
# hash_table.insert("banana", 20)
# hash_table.insert("orange", 30)
# hash_table.insert("melon", 40)
# hash_table.insert("grape", 50)
# hash_table.insert("pear", 60)
# hash_table.insert("peach", 70)

# # Retrieving values
# print(hash_table.get("banana"))  # Output: 20
# print(hash_table.get("orange"))  # Output: 30
# print(hash_table.get("peach"))   # Output: 70

# # Deleting a key-value pair
# hash_table.delete("banana")
# print(hash_table.get("banana"))  # Output: Not Found

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]
        
    def _hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self._hash_function(key)
        self.table[index].append((key,value))
        
    def get(self,key):
        index= self._hash_function(key)
        for k,v in self.table[index]:
            if k == key:
                return v
            else:
                print("Value not found")
                
    def delete(self,key):
        index = self._hash_function(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
            else:
                print("Not found")
                
a=HashTable(5)
a.insert('babana',65)
a.insert('babanga',34)
a.insert('d',87)
a.insert('f',43)
a.insert('fg',78)
a.insert('sd',12)
print(a.get('babana'))
print(a.delete('babana'))

print(a.get('babana'))
