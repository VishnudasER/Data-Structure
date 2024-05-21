
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(7)
print("7th Fibonacci number is:", result)  

def sum_of_digits(n):
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)


result = sum_of_digits(9)
print("Sum of digits in 12345 is:", result) 

def factorial(n):
    if n<=1:
        return n
    else:
        return n*factorial(n-1)
print(factorial(5))


def binary_search_recursive(arr,target,low,high):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid +1,high)
    else:
        return binary_search_recursive(arr,target,low,mid - 1)

arr = [1,2,3,4,5,6,7,8]
target = 6
result = binary_search_recursive(arr,target,0,len(arr)-1)
print("Position is at : ",result)