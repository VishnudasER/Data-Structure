def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    left_i,right_i=0,0
    while left_i<len(left) and right_i <len(right):
        if left[left_i] < right[right_i]:
            result.append(left[left_i])
            left_i +=1
        else:
            result.append(right[right_i])
            right_i +=1
    result.extend(left[left_i:])
    result.extend(right[right_i:])
    return result

arr = [54,5464,53,24,24254,3,4242,42]
arr=merge_sort(arr)
print(arr)

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Sample workouts
arr1 = [64, 25, 12, 22, 11]
arr2 = [38, 27, 43, 3, 9, 82, 10]
arr3 = [100, 90, 80, 70, 60, 50, 40]
arr4 = [5, 4, 3, 2, 1]
arr5 = [1, 2, 3, 4, 5]

merge_sort(arr1)
merge_sort(arr2)
merge_sort(arr3)
merge_sort(arr4)
merge_sort(arr5)

print("Sorted arrays:")
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
