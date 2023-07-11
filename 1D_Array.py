'''
1-D Array
- Declare array
- Enter values
- Delete value
'''

# Get the size of array
print("Enter the number of elements in an array",end=" ")
num = int(input())

# Declare an array
arr = []    

print("Enter", num, "Elements: ",end="")

# Enter elements into array
for i in range(num):
    element = input()
    arr.append(element)

# Delete an element by asking user
print("Enter the value to delete: ")
val = input()
if val in arr:
    arr.remove(val)
    print("New array is: ")
    for i in range(num-1):
        print(arr[i])
else:
    print("Element not found")