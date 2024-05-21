def Reverse_string(s):
    if len(s) <=1:
        return s
    else:
        return Reverse_string(s[1:])+ s[0]
        
original = "Hello World"
print(Reverse_string(original))

def Reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        return Reverse_string(string[1:]) + string[0]

result = "hi iam vishnu"
print(Reverse_string(result))