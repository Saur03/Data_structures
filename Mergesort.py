def merge_Sorting(arr):
    if len(arr) > 1:
        x = len(arr)//2
        l = arr[:x]
        r = arr[x:]
        #sorting the halves of array
        merge_Sorting(l)
        merge_Sorting(r)
        y = z = d = 0
        while y < len(l) and z < len(r):
            if l[y] <  l[z]:
                arr[d] = l[y]
                y += 1
            else:
                arr[d] = r[z]
                z += 1
            d += 1
        while y < len(l):
            arr[d] = l[y]
            y += 1
            d += 1
        while z < len(r):
            arr[d] = r[z]
            z += 1
            d += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
# Driver program
if __name__ == '__main__':
    arr = [11, 34, 2, 18, 33, 22, 88, 9]
    merge_Sorting(arr)
    print(" The sorted array is as follows: ")
    printList(arr)    

