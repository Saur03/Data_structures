'''
This program finds the index of first occurence of an element
for example: Arr = [1,1,1]; Output for 1 will be '0'
'''

import array
arr = array.array('u', ['c', 'a', 'b', 'd', 'e', 'f'])

print ("The new created array is : ", end = " ")
for i in range (0, 6):
    print (arr[i], end = " ")
print ("\r")
print (" The index of 1st occurrence of a is : ", end = "")
print (arr.index('a'))
print ("The index of 1st occurrence of f is :", end = "")
print (arr.index('f'))