print("Enter the number of elements in an array",end=" ")
num = int(input())
arr = []
print("Enter", num, "Elements: ",end="")

for i in range(num):
    element = input()
    arr.append(element)

print("The elements of array are: ")
for i in range(num):
    print(arr[i])