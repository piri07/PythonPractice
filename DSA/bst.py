class Node:
    def __init__(self,item):
        self.val=item
        self.right=self.left=None


def insert(root,node):
    if root is None:
        root=node
    
    else:
        if root.val<node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right,node)
        
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left,node)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

r = Node(10) 
insert(r,Node(5)) 
insert(r,Node(20)) 
insert(r,Node(40)) 
insert(r,Node(70)) 
insert(r,Node(60)) 
insert(r,Node(80))

inorder(r)