def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] <arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
        
    return arr

arr=[45,4,645,34,43645,6,335,35,353]
print("Unsorted One : ",arr)
arr=selection_sort(arr)
print("Sorted One : ", arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Sample workouts
arr1 = [64, 25, 12, 22, 11]
arr2 = [38, 27, 43, 3, 9, 82, 10]
arr3 = [100, 90, 80, 70, 60, 50, 40]
arr4 = [5, 4, 3, 2, 1]
arr5 = [1, 2, 3, 4, 5]

selection_sort(arr1)
selection_sort(arr2)
selection_sort(arr3)
selection_sort(arr4)
selection_sort(arr5)

print("Sorted arrays:")
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
