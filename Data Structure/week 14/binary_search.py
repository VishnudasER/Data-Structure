
def BS(key, arr):
    if len(arr) == 0:
        return -1  

    mid = len(arr) // 2

    if arr[mid] == key:
        return mid + 1
    elif arr[mid] < key:
        result = BS(key, arr[mid + 1:])
        return -1 if result == -1 else mid + 1 + result
    else:
        return BS(key, arr[:mid])

arr = [23, 56, 61, 62, 65, 67, 78, 90]
target = 78
print('Position is : ',BS(target, arr))


