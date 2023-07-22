# Insertion sort is one of the easiest and brute force sorting algorithm
# Insertion sort is used to sort the elements in either ascending order or in descending orde
# In insertion sort, we maintain a sorted part and unsorted part
# It worked lise playing cards i.e picking one card and sorting it with the cards that we have in our hand already which in turn are sorted
# With every iteration, one item from the unsorted part will move to the sorted part
# first element is picked and considered as sorted
# then we start picking the 2nd elements onwards and start comparing it with elements in sorted part
# We shift the elements from sorted by one element until an appropriate location is not found for the picked element
# this continued till all the elements gets exhausted

def insertion_Sort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array [j]
            j = j - 1
        array[j + 1] = key
data = [5, 2, 1, 7, 8]
insertion_Sort(data)
print('Sorted Array in Ascending Order: ')            
print(data)