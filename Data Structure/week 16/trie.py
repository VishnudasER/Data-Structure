class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Sample workout 1
trie1 = Trie()
words1 = ["apple", "banana", "orange", "app", "applesauce"]
for word in words1:
    trie1.insert(word)
print("Search results for sample workout 1:")
print("Is 'apple' in Trie?", trie1.search("apple"))  # True
print("Is 'app' in Trie?", trie1.search("app"))      # True
print("Is 'orange' in Trie?", trie1.search("orange"))# True
print("Is 'grape' in Trie?", trie1.search("grape"))  # False

# Sample workout 2
trie2 = Trie()
words2 = ["car", "cat", "dog", "dragon", "doghouse"]
for word in words2:
    trie2.insert(word)
print("\nSearch results for sample workout 2:")
print("Is 'dog' in Trie?", trie2.search("dog"))        # True
print("Is 'dragon' in Trie?", trie2.search("dragon"))  # True
print("Is 'apple' in Trie?", trie2.search("apple"))    # False

# Sample workout 3
trie3 = Trie()
words3 = ["python", "java", "javascript", "ruby", "c"]
for word in words3:
    trie3.insert(word)
print("\nSearch results for sample workout 3:")
print("Is 'java' in Trie?", trie3.search("java"))          # True
print("Is 'python' in Trie?", trie3.search("python"))  # False
print("Is 'ruby' in Trie?", trie3.search("ruby"))          # True

