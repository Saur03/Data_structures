print("Enter the number of elements in an array",end=" ")
num = int(input())
arr = []
print("Enter", num, "Elements: ",end="")

for i in range(num):
    element = input()
    arr.append(element)

print("Enter the value to delete: ")
val = input()
if val in arr:
    arr.remove(val)
    print("New array is: ")
    for i in range(num-1):
        print(arr[i])
else:
    print("Element not found")