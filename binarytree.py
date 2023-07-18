# Implementation of binary tree useing inorder, post order and pre-order traversal

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
        
    # Implementation of preorder is print, left and then rigjht
    def traPreorder(self):
        print(self.val, end= ' ')
        if self.left:
            self.left.traPreorder()
        if self.right:
            self.right.traPreorder()

    # Implementation of Inorder is left, print and then right  
    def traInorder(self):
        if self.left:
            self.left.traInorder()
        print(self.val, end= ' ')
        if self.right:
            self.right.traInorder()

    # implementation of post order is left, right and print 
    def traPostorder(self):
        if self.left:
            self.left.traPostorder()
        if self.right:
            self.right.traPostorder()
        print(self.val, end= ' ')


root = Node(1)
root.left = Node(2)
root.right  = Node(3)
root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traPreorder()
print("\n In order Traversal: ", end="")
root.traInorder()
print("\n Post order Traversal: ", end="")
root.traPostorder()
