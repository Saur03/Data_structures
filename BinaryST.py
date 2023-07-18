#Implementation of binary search tree

# Created a class Node and called init method
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None

# Inorder traversal function
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end= ' ')
        inorder(root.right)

# Insert a node to the tree
def insert(node, key):

    # return a new node if the tree is empty or null
    if node is None:
        return Node(key)

    # Traverse and insert the node in the right place
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right,key)

    return node

# Find the inorder succesor is defined or the size 
def minValueNode(node):
    current = node

    # Find the leftmost leaf is node
    while(current.left is not None):
        current = current.left

    return current

# Deletion a node is done
def deleteNode(root, key):

    # Return back if the tree is empty
    if root is None:
        return root

    # Find the node to be deleted from the tree
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        # if the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.right
            root = None
            return temp

         # If the node has two children
         # place the inorder successor in position of the node to be deleted
        temp = minValueNode(root.right)

        root.key = temp.key

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp,key)

    return root            

    
root = None
root = insert(root, 9)
root = insert(root, 4)
root = insert(root, 2)
root = insert(root, 7)
root = insert(root, 8)
root = insert(root, 11)
root = insert(root, 15)
root = insert(root, 5)

print("Inorder traversal: ", end =' ')
inorder(root)
print("\nDelete 11")
root = deleteNode(root, 11)
print("Inorder traversal: ", end = ' ')
inorder(root)

