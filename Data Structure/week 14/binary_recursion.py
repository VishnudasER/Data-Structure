
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


def binary_search_recursive(arr,target,low,high):
    if low >= high:
        return -1
    mid = (low+high) // 2
    if arr[mid] ==target:
        return mid +1
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid + 1, high)
    else:
        return binary_search_recursive(arr,target,low, mid -1)

arr=[2,3,4,5,6,7,9]
target=5
result=binary_search_recursive(arr,target,0,len(arr)-1)
print(result)

def binary_search_recursive(arr,target,low,high):
    if low >= high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid +1
    elif arr[mid] < target:
        return binary_search_recursive(arr,target, mid + 1, high)
    else:
        return binary_search_recursive(arr,target,low, mid -1)

arr= [1,2,3,4,5,6,9,11]
target = 6
li=binary_search_recursive(arr,target,0,len(arr)-1)
print(li)

def binary_search_recursive(arr,target,low,high):
    if low>=high:
        return -1
    mid = (low+high) //2
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] < target:
        return binary_search_recursive(arr,target,mid +1,high)
    else:
        return binary_search_recursive(arr,target,low,mid-1)
    
arr = [1,2,3,4,5,6]
target = 3
li=binary_search_recursive(arr,target,0,len(arr)-1)
print(li)