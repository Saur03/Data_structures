r = int(input("Enter the number of rows: "))
c = int(input("Enter the number of columns: "))
twod_arr = [[0 for col in range(c)] for row in range(r)]

for row in range(r):
    for col in range(c):
        twod_arr[row][col] = row*col
print(twod_arr)