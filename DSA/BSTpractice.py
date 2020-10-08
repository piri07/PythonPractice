#check if a tree is BST or not

mini=-9999
maxi=99999

class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def isBSTUtil(root,mini,maxi):
    
    if root is None:
        return True
    if root.val<mini or root.val>maxi:
        return False

    return (isBSTUtil(root.left,mini,root.val-1) and isBSTUtil(root.right,root.val+1,maxi))

def isBST(root):
    return isBSTUtil(root,mini,maxi)


root = Node(4) 
root.left = Node(2) 
root.right = Node(5) 
root.left.left = Node(1) 
root.left.right = Node(3) 
  
if (isBST(root)): 
    print("Is a BST")
else: 
    print("is not a BST")


##################################################################################################################################################################33

#check array if is represent inorder BST or not
#inorder traversal of BST gives a sorted list

def isInorder(arr,n):
    if n==0 or n==1:
        return True
    
    for i in range(1,n):
        if arr[i-1]>arr[i]:
            return False
    return True

arr = [19, 23, 25, 30, 45] 
n = len(arr) 
      
if (isInorder(arr, n)): 
    print("Yes") 
else: 
    print("No")

################################################################################################################################################################################################33

#lowest common ancestor in a bst

def lca(root,n1,n2):
    if root is None:
        return root

    if root.val>n1 and root.val>n2:
        return lca(root.left,n1,n2)

    if root.val<n1 and root.val<n2:
        return lca(root.right,n1,n2)

    return root

root = Node(20) 
root.left = Node(8) 
root.right = Node(22) 
root.left.left = Node(4) 
root.left.right = Node(12) 
root.left.right.left = Node(10) 
root.left.right.right = Node(14)

n1 = 10 ; n2 = 14
t = lca(root, n1, n2) 
print("LCA of %d and %d is %d" %(n1, n2, t.val)) 
  
n1 = 14 ; n2 = 8
t = lca(root, n1, n2) 
print("LCA of %d and %d is %d" %(n1, n2 , t.val))
  
n1 = 10 ; n2 = 22
t = lca(root, n1, n2) 
print("LCA of %d and %d is %d" %(n1, n2, t.val)) 


##############################################################################################################################################################################

#convert normal bst to balanced BSt

def storeVal(root,nodes):
    if not root:
        return

    storeVal(root.left,nodes)
    nodes.append(root)
    storeVal(root.right,nodes)

def buildTreeUtil(nodes,start,end):
    if start>end:
        return None

    mid = (start+end)//2
    root =nodes[mid]
    root.left = buildTreeUtil(nodes,start,mid-1)
    root.right =buildTreeUtil(nodes,mid+1,end)
    return root

def buildTree(root):
    if not root:
        return 

    nodes = []
    storeVal(root,nodes)
    n=len(nodes)
    return buildTreeUtil(nodes,0,n-1)
def preorder(root):
    if not root:
        return
    print(root.val,end=" ")
    preorder(root.left)
    preorder(root.right)

root = Node(10) 
root.left = Node(8) 
root.left.left = Node(7) 
root.left.left.left = Node(6) 
root.left.left.left.left = Node(5) 
root = buildTree(root) 
print("Preorder traversal of balanced BST is :") 
preorder(root)

###############################################################################################################################################################################

# Python3 code to find the largest 
# value smaller than or equal to N 
class newNode: 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None

def insert(node, key): 
 
	if node == None: 
		return newNode(key) 
	if key < node.key: 
		node.left = insert(node.left, key) 
	elif key > node.key: 
		node.right = insert(node.right, key) 
		 
	return node 

def findMaxforN(root, N): 
	
	# Base cases 
	if root == None: 
		return -1
	if root.key == N: 
		return N 
	elif root.key < N: 
		k = findMaxforN(root.right, N) 
		if k == -1: 
			return root.key 
		else: 
			return k 

	elif root.key > N: 
		return findMaxforN(root.left, N) 


if __name__ == '__main__': 
	N = 4

	root = None
	root = insert(root, 25) 
	insert(root, 2) 
	insert(root, 1) 
	insert(root, 3) 
	insert(root, 12) 
	insert(root, 9) 
	insert(root, 21) 
	insert(root, 19) 
	insert(root, 25) 
	print(findMaxforN(root, N)) 

##################################################################################################################################################################################

def insertt(root,key):
    if root==None:
        root = newNode(key)

    elif key>root.key:
        root.right = insertt(root.right,key)
    elif key<root.key :
        root.left = insertt(root.left,key)
    return root
def height(root,x):
    if root.key ==x:
        return 0
    elif root.key>x:
        return 1+ height(root.left,x)
    return 1+height(root.right,x)

def distBtw(root,a,b):
    if root==None:
        return 0
    if root.key>a and root.key>b:
        return distBtw(root.left,a,b)
    if root.key<a and root.key<b:
        return distBtw(root.right,a,b)
    if root.key>=a and root.key<=b:
        return height(root,a) + height(root,b)

def findDistWrapper(root, a, b): 
    if a > b: 
        a, b = b, a  
    return distBtw(root, a, b) 




if __name__ == '__main__': 
    root = None
    root = insert(root, 20)  
    insert(root, 10)  
    insert(root, 5)  
    insert(root, 15)  
    insert(root, 30)  
    insert(root, 25)  
    insert(root, 35) 
    a, b = 5, 55
    print(findDistWrapper(root, 5, 35))

#####################################################################################################################################################################################

#find pair given sum in a BST
class Node1: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None
def inserttt(root,data): 
    if root is None: 
        return Node1(data) 
    if(data < root.data): 
        root.left = insert(root.left, data) 
    if(data > root.data): 
        root.right = insert(root.right, data) 
    return root 
  
def findPairUtil(root, summ, unsorted_set): 
    if root is None: 
        return False
    if findPairUtil(root.left,summ,unsorted_set): 
        return True
    if unsorted_set and (summ-root.data) in unsorted_set: 
        print("Pair is Found ({},{})".format(summ-root.data, root.data)) 
        return True
    else: 
        unsorted_set.add(root.data) 
  
    return findPairUtil(root.right,summ, unsorted_set) 
  
def findPair(root,summ): 
    unsorted_set = set() 
    if(not findPairUtil(root,summ,unsorted_set)): 
        print("Pair do not exist!") 
  
# Driver code 
if __name__=='__main__': 
    root=None
    root = inserttt(root,15) 
    root = inserttt(root,10) 
    root = inserttt(root,20) 
    root = inserttt(root,8) 
    root = inserttt(root,12) 
    root = inserttt(root,16) 
    root = inserttt(root,25) 
    root = inserttt(root,10) 
    summ = 33
    findPair(root, summ) 

##########################################################################################################################################################################################3333

