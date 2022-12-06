# functions with parameters
def hashing_key( key, m):
    #modulus operation to find hash value
    return key % m
# the size of the hash table
m = 8
print(f'The hash vaalue for 4 is {hashing_key(4,m)}' )
print(f'The hash vaalue for 3 is {hashing_key(3,m)}' )
print(f'The hash vaalue for 10 is {hashing_key(10,m)}' )
print(f'The hash vaalue for 12 is {hashing_key(12,m)}' )
print(f'The hash vaalue for 8 is {hashing_key(8,m)}' )


