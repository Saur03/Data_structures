# functions with parameters
# hashing is a black box that takes key as input and provides hash value as output, where hash value belongs to a fixed space.
# it is a one way function
# A hash table is a data structure that uses a pair of keys and values to store values, each value is given a one-of-a-kind key created by a hash function
def hashing_key( key, m):
    #modulus operation to find hash value
    return key % m
# the size of the hash table
m = 8
print(f'The hash value for 4 is {hashing_key(4,m)}' )
print(f'The hash value for 3 is {hashing_key(3,m)}' )
print(f'The hash value for 10 is {hashing_key(10,m)}' )
print(f'The hash value for 12 is {hashing_key(12,m)}' )
print(f'The hash value for 8 is {hashing_key(8,m)}' )


