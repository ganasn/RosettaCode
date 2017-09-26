#MergeSort.py

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while(left_idx < len(left) and right_idx < right(right)):
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
        return result

    
    while(len(left) > 0 and len(right) > 0):
        if left[0] <= right[0]:
            array.push(left[0])
            left = left[1:]
        else:
            array.push(right[0])
            right = right[1:]
        if len(left) > 0:
            array.push(left)
        if len(right) > 0:
            array.push(right)
        return array

def merge_sort(array):
    if len(array) <= 1: 
        return array
    
    size = len(array)//2
    left = list()
    right = list()
    left = array[:size]
    right = array[size:]
    print(left)
    print(right)
    left = merge_sort(left)
    right = merge_sort(right)
    array = merge(left, right)
    return array
    


#    i = 0
#    j = 0
##    print(left[i], right[j])
#    for counter in range(0, len(array)):
#        print(i, j)
#        print(array)    
#        while 
#        for i in range(0, size-1):
#        if(i <= size-1 and left[i] <= right[j]):
#            array[counter] = left[i]
#            i += 1
#        else:
#            array[counter] = right[j]
#            j += 1
#    print(array)    



array = list()
array = [11, 1, 4, 2, 5, 3, 10]
merge_sort(array)