#http://rosettacode.org/wiki/Sorting_algorithms/Insertion_sort
#Sorting Algorithms - Insertion Sort
#
#function insertionSort(array A)
#    for i from 1 to length[A]-1 do
#        value := A[i] 
#        j := i-1
#        while j >= 0 and A[j] > value do
#            A[j+1] := A[j]
#            j := j-1
#        done
#        A[j+1] = value
#    done


def insertion_sort(array):
    for j in range(1, len(array)):
        key = array[j]
#        print j, key
        i = j - 1
        while ((i >= 0) and array[i] > key):
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
        print array
        
array = list()
array = [11, 1, 4, 2, 5, 3, 10]
print 'original array ', array
#print '# of elements ', len(array)
insertion_sort(array)
print 'sorted array ', array