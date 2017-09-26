#BubbleSort.py

def bubble_sort(array):
    for counter1 in range(0, len(array)-1):
#        print('Counter1 value - ', counter1)
        for counter2 in range(len(array)-1, counter1, -1):
#            print('Counter2 value - ', counter2)
#            print('array[counter2]', array[counter2])
#            print('array[counter2-1]', array[counter2-1])
            if array[counter2] < array[counter2-1]:
                
                array[counter2], array[counter2-1] = array[counter2-1], array[counter2]
#    print(array)
    return array

array = list()
array = [11, 1, 4, 2, 5, 3, 10]
print('original array', array)
bubble_sort(array)
print('sorted array', array)
