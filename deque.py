'''
Stack from Deque
functions: append, pop, appendleft, popleft, reverse
'''

from collections import deque
stack=deque()
stack.append("x")
print(stack)
stack.append("y")
stack.append("z")
print(stack)
print(stack.pop())
print(stack)
stack.appendleft("a")
print(stack)
stack.popleft()
print(stack)
stack.reverse()
print(stack)