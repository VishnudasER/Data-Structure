def Palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return Palindrome(string[1:-1])

string="malayalam"
print(Palindrome(string))

def Palindrome(string):
    if len(string)<=1:
        return True
    if string[0] != string[-1]:
        return False
    return Palindrome(string[1:-1])

string="ab"
print(Palindrome(string))
    
def palindrone(string):
    if len(string)<=1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrone(string[1:-1])


def palindrome(string):
    if len(string)<=1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome(string[1:-1])

string = "malayalam"
print(palindrome(string))

def Palindrome(string):
    if len(string)<=1:
        return True
    if string[0] != string[-1]:
        return False
    return Palindrome(string[1:-1])

def palindrome(s):
    if len(s)<=1:
        return True
    if s[0] != s[-1]:
        return False
    return Palindrome(s[1:-1])
s='sksks'
print(palindrome(s))