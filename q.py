'''
Create Stack from LIFOQUEUE
Functions : put, get, qsize, full, empty
'''

from queue import LifoQueue
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