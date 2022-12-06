def selectionSort(array, size):
    for step in range(size):
        min = step
        for i in range(step + 1, size):
            if array[i] < array[min]:
                min = i
        # this is used to put minimum number in correct position
        (array[step], array[min]) = (array[min], array[step]) 

data = [-20, 45, 12, 22, 19]
size = len(data)
selectionSort(data, size)
print(' Sorted array using selection sort in ascending order: ')
print(data)


