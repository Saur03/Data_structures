# Binary search is one of the searching algorithm
# it can be used on sorted array
# this searching technique follows the divide and conquer stategy and search space always always reduce to half in every iteration
# this is a very efficient technique for searching but it needs some order on which partition of array will occur
# Binary Search in python
def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high -low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1
    return -1
array = [3, 4, 5, 6, 7, 8, 9]
x=4
result = binarySearch(array,x, 0, len(array)-1) 
if result != -1:
    print("Element is preent at index " + str(result))
else:
    print("Not found")                        
