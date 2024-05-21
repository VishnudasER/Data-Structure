def quick_sort(arr):
    if len(arr) <=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

arr= [45,4,6435,33,53,5,35,3,523]
arr=quick_sort(arr)
print(arr)

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x< pivot]
    middle =[x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) +middle + quick_sort(right)

arr= [45,4,6435,33,53,5,35,3,523]
arr=quick_sort(arr)
print(arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Sample workouts
arr1 = [64, 25, 12, 22, 11]
arr2 = [38, 27, 43, 3, 9, 82, 10]
arr3 = [100, 90, 80, 70, 60, 50, 40]
arr4 = [5, 4, 3, 2, 1]
arr5 = [1, 2, 3, 4, 5]

sorted_arr1 = quick_sort(arr1)
sorted_arr2 = quick_sort(arr2)
sorted_arr3 = quick_sort(arr3)
sorted_arr4 = quick_sort(arr4)
sorted_arr5 = quick_sort(arr5)

print("Sorted arrays:")
print(sorted_arr1)
print(sorted_arr2)
print(sorted_arr3)
print(sorted_arr4)
print(sorted_arr5)
