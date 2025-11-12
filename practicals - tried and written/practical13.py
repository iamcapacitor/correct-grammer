'''
Implement various operations on a Binary Search Tree, such as 
search
display, 
insertion, 
deletion, 
'''

class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

class BinarysearchTree:
    def __init__(self):
        print("Initializing Binary Search Tree")
        self.rootnode = None

    def search(self , root , data):
        if root is None or root.data == data:
            return root
        elif data < root.data:
            return self.search(root.left , data)
        elif data > root.data:
            return self.search(root.right , data)
    
    def Inordertraversal(self , root):
        if root:
            self.Inordertraversal(root.left)
            print(root.data , end=" ")
            self.Inordertraversal(root.right)
    
    def insert(self ,root, data):
        if root == None:
            print(f"Node with {data} inserted successfully")
            return Node(data)
        elif data < root.data:
            root.left = self.insert(root.left , data)
        elif data > root.data:
            root.right = self.insert(root.right , data)
        return root # this is returned if no data is inserted
    
    def Minvaluenode(self , node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def deletenode(self , root , data):
        if root is None:
            return root
        
        if data < root.data:
            root.left = self.deletenode(root.left , data)
        elif data > root.data:
            root.right = self.deletenode(root.right , data)
        else:

            # case 1 ,2 = no children or one children
            if root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            
            # case 3 = two children
            temp = self.Minvaluenode(root.right)
            root.data = temp.data
            root.right = self.deletenode(root.right , temp.data)
        return root

# --- Demonstration --------------------
bst = BinarysearchTree()

keys = [50,60,70,12,5,29,30,35]
root = None
for key in keys:
    root = bst.insert(root,key)

bst.Inordertraversal(root)
root = bst.deletenode(root , 5)
print()
bst.Inordertraversal(root)


