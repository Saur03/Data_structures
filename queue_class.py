'''
Queue is first in first out (FIFO), example - ticket counters and bus stations.
In queue, there are 4 operations:-
1. enqueue() - used to insert at top
2. dequeue() - delete the top element from the queue
3. peekfirst() - to get the first element of queue
4. peeklast() - to get the last element of queue

time complexity is of 0(1)
'''
'''
Create a class queue to perform enqueue and dequeue operations and use append and pop functions for insertion and deletion of an element
'''
#created a class queue and in this, there are 5 functions performed like init, queue, dequeu , display and size:-
class Queue:
    def __init__(self):
        self.queue = []
    def enqueu(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

q = Queue()
q.enqueu(1)   
q.enqueu(2)        
q.enqueu(3)        
q.enqueu(4)        
q.enqueu(5)    
q.display()
q.dequeue()
print("After removing an element")
q.display()   
