# Transversal in linked list

class Node:
    def __init__ (self,data):
        self.data=data   #n1.data=5,n2.data=10,n3.data=15,n4.data=20
        self.next=None   #n1.next=None,n2.next=None,n3.next=None,n4.next=None

class Sll:
    def __init__(self):
        self.head=None  #sll.head=None

    def traversal(self):
        if self.head is None:
            print("Singly linked list is empty")
        else:
            a=self.head                      #a=sll.head
            while a is not None:             #a=sll.head=n1 #a=n1.next  
                print(a.data, end= " ")      #a.data=n1.data    
                a=a.next                     #a=n1.next, a=n2.next, a=n3.next

n1=Node(5)
sll=Sll()
sll.head=n1
n2=Node(10)
n1.next=n2                   
n3=Node(15)
n2.next=n3
n4=Node(20)
n3.next=n4  
sll.traversal()         


