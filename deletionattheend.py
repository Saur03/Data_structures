# Creating a singly linked list with insertion at the end.
class Node:
    def __init__ (self,data):
        self.data=data   #n1.data=5,n2.data=10,n3.data=15,n4.data=20,nb.data=2,ne.data=25,nib=7
        self.next=None   #n1.next=None,n2.next=None,n3.next=None,n4.next=None,nb.next=None,ne.next=None,nib.next=None

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

    def insert_at_beginning(self,data):      #data=2
        print()
        nb=Node(data)                        #nb.Node(2)
        nb.next=self.head                    #nb.next=n1
        self.head=nb                         #sll.head=nb

    def insert_at_end(self,data):            #data=25    
        print()
        ne=Node(data)
        a=self.head                          #a-sll.head=nb
        while a.next is not None:            #a.next=nb.next  #n1.next    
            a=a.next                         #a=nb.next=n1 #a=n2
        a.next=ne                            #n4.next=ne

    def insertion_at_specified_node(self,position,data):  #position=3,data=7
        print()
        nib=Node(data)
        a=self.head                #a=sll.head=nb
        for i in range(1,position-1):             #i=1
            a=a.next                              #a=nb.next=n1
            nib.next=a.next                       #nib.next=n1.next=n2
            a.next=nib                            #a.next=n1.next=nib

    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None

    def deletion_at_end(self):
        print()
        # in the below syntax, firstly we have created a variable "prev" and given head to that and checking with while loofp that the data of the node is none or not,if none, we have delete the last node
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None    


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
sll.insert_at_beginning(2)
sll.traversal()
sll.insert_at_end(25)
sll.traversal()
sll.insertion_at_specified_node(3,7)
sll.traversal()
sll.deletion_at_beginning()
sll.traversal()
sll.deletion_at_end()
sll.traversal()