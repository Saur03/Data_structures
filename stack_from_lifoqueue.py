'''
Create Stack from LIFOQUEUE
Functions : put, get, qsize, full, empty
'''
# Queue module contains the LIFO queue.
# have additional functions like put, get, qsize, full, maxsize and empty

from queue import LifoQueue

#created the variable stack
stack=LifoQueue(maxsize=3)
stack.put(2)
stack.put(3)
stack.put(4)
print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())
print(stack.empty())
stack.get()
stack.get()
print(stack.empty())
 