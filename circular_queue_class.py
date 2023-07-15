'''
Create class for circular queue
Usage: enqueue, dequeue

initialise queue for size k
head and tail starts from -1
'''

class circularQueue():
    # constructor
    def __init__(self, k):
        self.k =k
        # initialising queue with none
        self.queue = [None] * k
        self.head = self.tail = -1

    def enqueue(self, data):
        # condition if queue is full
        if ((self.tail + 1) % self.k) == self.head:     #overlap tail, if meets with head
            print("Circular queue is full\n")
            
        # condition for empty queue
        elif (self.head == -1):                         # head not > 0; no element present
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:        
            # next position of tail                     # at least 1 element and not full
            self.tail = (self.tail + 1) % self.k                
            self.queue[self.tail] = data
    
    def dequeue(self):
        # Condition for empty queue
        if (self.head == -1):                           # no element to pop
            print("Circular queue is empty\n")
            
        # Condition for only onr element    
        elif (self.head == self.tail):                  # 1 element to pop
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:                                           # more than 1 element to pop
            temp = self.queue[self.head]
            self.head = (self.head +1) % self.k
            return temp
        
    def printQueue(self):
        
        # Condition for empty queue
        if (self.head == -1):                           # no element
            print("Circular queue is empty\n")
        
        elif (self.tail >= self.head):                  # simple case where head never moves; enqueue
            for i in range(self.head, self.tail+1):
                print(self.queue[i], end=" ")
            print()
        else:                                           # case where queue gets full and then we dequeue to make space  and then enqueue to wrap tail
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail +1):
                print(self.queue[i], end=" ")
            print()

# Driver code
obj = circularQueue(5)
obj.enqueue(10)
obj.enqueue(20)
obj.enqueue(30)
obj.enqueue(40)
obj.enqueue(50)
print("Initial Circular queue\n")
obj.printQueue()

obj.dequeue()
obj.dequeue()
print("New Circular queue\n")
obj.printQueue()
obj.enqueue(60)
obj.enqueue(70)
obj.printQueue()