## BST - Recursion
# - Tree creation, node insertion
# - Inorder traversal 
# - Search element exists
# - Delete node

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None
        

class BST:
    
    def __init__(self) -> None:
        self.root = None
    
    def insert_element(self,data):
        
        def _insert(root,data):
            if root is None:
                return Node(data)
            elif root.data > data:
                root.left = _insert(root.left,data)
            elif root.data < data:
                root.right = _insert(root.right,data)
                
            return root
            
        self.root = _insert(self.root,data)
        
    def inorder_traversal(self):
        
        def _inorder(root):
            if root.left is None and root.right is None:
                print(root.data, end=' ')
                return
            if root.left is not None:
                _inorder(root.left)
            print(root.data, end=' ')
            if root.right is not None:
                _inorder(root.right)

        _inorder(self.root)

    def search_element(self,value):
        
        if self.root is None:
            print('BST is empty')
            return False
        def _search(root,val):
            if root is None:
                return False
            elif root.data == val:
                return True
            elif root.data > val:
                 return _search(root.left,val)
            elif root.data < val:
                return _search(root.right,val)        
        return _search(self.root,value)
        
        
#Tree creation--------------------------------------------
bst = BST()
bst.insert_element(2)
bst.insert_element(1)
bst.insert_element(3)
bst.insert_element(4)
bst.insert_element(3.5)
bst.insert_element(0.5)
# print(bst)

#Inorder traversal--T(O): O(n)-----------------------------------------

bst.inorder_traversal()

#Search element--T(O): log(n)-----------------------------------------
print(end='\n')
print(bst.search_element(4))