def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

arr= [54,7,65,35,465,654,5]
array=insertion_sort(arr)
print(arr)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Sample workouts
arr1 = [12, 11, 13, 5, 6]
arr2 = [38, 27, 43, 3, 9, 82, 10]
arr3 = [100, 90, 80, 70, 60, 50, 40]
arr4 = [5, 4, 3, 2, 1]
arr5 = [1, 2, 3, 4, 5]

insertion_sort(arr1)
insertion_sort(arr2)
insertion_sort(arr3)
insertion_sort(arr4)
insertion_sort(arr5)

print("Sorted arrays:")
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
