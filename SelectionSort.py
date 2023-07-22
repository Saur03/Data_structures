# Selection sort is a simple sort algorithm that revolves around the 'comparison'
# In each iteration, one element gets placed.
# We choose the minimum element in the array and place is at the beginning of the array by swapping with the front elemant
# We can also do this by choosing maximum element and placing it at the rear end.
# Selection sort basically selects an element in every iteration and place it at the appropriate position.
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


