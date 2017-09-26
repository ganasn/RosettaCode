#MergeSort.py

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while(left_idx < len(left) and right_idx < len(right)):
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
        if left_idx < len(left):
            result.extend(left[left_idx:])
        if right_idx < len(right):
            result.extend(right[right_idx:])
        print('Result', result)
        return result

def merge_sort(array):
    if len(array) <= 1: 
        return array
    
    size = len(array)//2
    left = list()
    right = list()
    left = array[:size]
    right = array[size:]
    print('left', left)
    print('right', right)
    left = merge_sort(left)
    right = merge_sort(right)
    array = merge(left, right)
    return array
    
array = list()
array = [11, 1, 4, 2, 5, 3, 10]
print("Original array", array)
merge_sort(array)
print("Sorted array", array)