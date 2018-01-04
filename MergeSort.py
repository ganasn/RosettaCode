##MergeSort.py
#
#def merge(left, right):
#    result = []
#    left_idx, right_idx = 0, 0
#    while(left_idx < len(left) and right_idx < len(right)):
#        if left[left_idx] <= right[right_idx]:
#            result.append(left[left_idx])
#            left_idx += 1
#        else:
#            result.append(right[right_idx])
#            right_idx += 1
#        if left_idx < len(left):
#            result.extend(left[left_idx:])
#        if right_idx < len(right):
#            result.extend(right[right_idx:])
#        print('Result', result)
#        return result
#
#def merge_sort(array):
#    if len(array) <= 1: 
#        return array
#    
#    size = len(array)//2
#    left = list()
#    right = list()
#    left = array[:size]
#    right = array[size:]
#    print('left', left)
#    print('right', right)
#    left = merge_sort(left)
#    right = merge_sort(right)
#    array = merge(left, right)
#    return array
#    
#array = list()
#array = [11, 1, 4, 2, 5, 3, 10]
#print("Original array", array)
#merge_sort(array)
#print("Sorted array", array)


# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r- m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , n1):
        L[i] = arr[l + i]
 
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr,l,r):
    if l < r:
 
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        m = (l+(r-1))/2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)
        
        
# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print ("Given array is")
for i in range(n):
    print ("%d" %arr[i]),
 
mergeSort(arr,0,n-1)
print ("\n\nSorted array is")
for i in range(n):
    print ("%d" %arr[i]),