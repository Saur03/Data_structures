'''
This program finds the index of first occurence of an element
for example: Arr = [1,1,1]; Output for 1 will be '0'
'''

import array
#Created an array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print ("The new created array is : ", end = " ")
for i in range (0, 6):
    print (arr[i], end = " ")
print ("\r")
print (" The index of 1st occurrence of 2 is : ", end = "")
print (arr.index(2))
# it will only count first occurence not the second tim,if the numbers are repeated.
print ("The index of 1st occurrence of 1 is :", end = "")
print (arr.index(1))
