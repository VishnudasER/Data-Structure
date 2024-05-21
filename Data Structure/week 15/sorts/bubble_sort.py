def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] , arr[j]
    return arr

arr = [6,5,6434,42,4,86]
result=bubble_sort(arr)
print(result)

arr_string=["apple","borange","anana"]
bubble_sort(arr_string)
print(arr_string)

def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

arr=[54,4465,5,3,3,434]
arr=bubble_sort(arr)
print(arr)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr1 = [64, 34, 25, 12, 22, 11, 90]
arr2 = [5, 2, 8, 7, 1, 3, 9]
arr3 = [10, 20, 30, 40, 50]
arr4 = [5, 4, 3, 2, 1]
arr5 = [1, 2, 3, 4, 5]

bubble_sort(arr1)
bubble_sort(arr2)
bubble_sort(arr3)
bubble_sort(arr4)
bubble_sort(arr5)

print("Sorted arrays:")
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)



def bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

arr=[7,56,4564,53,3,4,35,46,45]
arr=bubble_sort(arr)
print(arr)


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j >= 0 and key< arr[j]:
            arr[j+1] = arr[j]
            j-=1
            arr[j+1] = key
    return arr


arr=[7,56,4564,53,3,4,35,46,45]
arr=insertion_sort(arr)
print(arr)

def selection_sort(arr):
    for i in range(1,len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr


arr=[7,56,4564,53,3,4,35,46,45]
arr=selection_sort(arr)
print(arr)

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


arr=[7,56,4564,53,3,4,35,46,45]
arr=quick_sort(arr)
print(arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    left_index,right_index = 0,0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index+=1
        else:
            result.append(right[right_index])
            right_index+=1
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result


arr=[7,56,4564,53,3,4,35,46,45]
arr=merge_sort(arr)
print(arr)
