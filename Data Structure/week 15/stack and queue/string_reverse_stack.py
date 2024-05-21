class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def reverse_string(string):
    stack = Stack()
    reversed_string = ""
    
    # Push each character onto the stack
    for char in string:
        stack.push(char)
    
    # Pop characters from the stack to construct the reversed string
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

# Example usage:
string = "Hello, World!"
reversed_string = reverse_string(string)
print("Original string:", string)
print("Reversed string:", reversed_string)


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

def is_palindrome(string):
    stack = Stack()
    string=string.lower()
    reversed_string = ""
    for char in string:
        stack.push(char)

    while not stack.is_empty():
        reversed_string += stack.pop()

    return string == reversed_string

# Test the function
input_string = "Radar"
print(f"'{input_string}' is a palindrome:", is_palindrome(input_string))

input_string = "hello"
print(f"'{input_string}' is a palindrome:", is_palindrome(input_string))
