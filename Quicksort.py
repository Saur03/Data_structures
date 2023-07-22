# Quick sort is one of the most widely used sorted algorithm
# It follow divide and rule paradigm
# Recursion is used in quicksort implementation
# In each recurion call, a pivot is chosen then the array is partitioned in such a way that all the elements less than pivot lie to the left and all the elements greater than pivot lie to the right
# After every call , the chosen pivot occupies its correct position in the array which it is supposd to as in sorted array
# So with each step, our problem gets reduced by 2 which leads to quick sorting
# pivot can be last element of current array, first element of current array, or any random element 
# Partition position finding function
def partition(arr, l, h):
    # right most element = pivot
    pivot = arr[h]
    # pointer for greater element
    i = l -1
    #Traverse all the elememts in the array and compare with pivot
    for j in range(l, h):
        if arr[j] <= pivot:
            # if smaller element is present than pivot then swap
            i = i + 1
            # swapping i with j
            (arr[i], arr[j]) = (arr[j], arr [i])
    # swap pivot with i if its greater than pivot
    (arr[i + 1], arr[h]) = (arr[h], arr[i + 1])
    #get back to the initial position where partition was done
    return i + 1

# quick sort function
def quick_Sort(arr, l, h):
    if l < h:
        #smaller element than pivot --> left
        #greater element than pivot --> right
        pi = partition(arr, l, h)
        # left of pivot recursion call
        quick_Sort(arr, pi + 1, h)

d = [9, 8, 7, 2, 10, 20, 1]
print("Unsorted Array")
print(d)
size = len(d)
quick_Sort(d, 0, size - 1)
print(' Sorted array in ascending order using quick sort: ')
print(d)                