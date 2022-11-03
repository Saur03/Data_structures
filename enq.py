'''
Create a class for queue to enqueu and dequeue elements
example: append and pop elements
'''

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