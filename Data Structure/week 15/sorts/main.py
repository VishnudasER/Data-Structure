def merge_sort(arr):
    if len(arr) <=1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    left_index,right_index =0,0
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

array =[6,4,35,4,435,5]
array=merge_sort(array)
print(array)
