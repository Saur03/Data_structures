class Node:
    def __init__(self,data):      #n1,5  #n2,10
        self.data=data
        self.next=None
        self.prev=None

class Dll:
    def __init__(self):
        self.head=None

    def forward_traversal(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data, end=" ")
                a=a.next

    def backward_traversal(self):
        print()
        if self.head is None:
            print("doubly linked list is empty")
        else:
            a=self.head                    #dll.head=n1
            while a.next is not None:      #n1.next
                a=a.next                   #a=n2   #a=n4 
            while a is not None:
                print(a.data, end=" ")
                a=a.prev  

    def insertion_at_beginning(self,data):
        print()
        ns=Node(data)
        a=self.head
        a.prev=ns
        ns.next=a
        self.head=ns     

    def insertion_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
        ne.prev=a               
                                 
n1=Node(5)
dll=Dll()
dll.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(15)
n3.prev=n2
n2.next=n3
n4=Node(20)
n4.prev=n3
n3.next=n4
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_beginning(2)
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_end(25)
dll.forward_traversal()
dll.backward_traversal()
