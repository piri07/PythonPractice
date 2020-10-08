#check if the given array can represent preorder traversal of bst

int_min=-99999

def canRepresentBST(pre):
    s=[]
    root=int_min

    for i in pre:
        if i<root:
            return False

        while len(s)>0 and s[-1]<i:
            root=s.pop()
        s.append(i)
    return True

pre1 = [40 , 30 , 35 , 80 , 100] 
if canRepresentBST(pre1) == True:
    print("true") 
else:
    print("false")


########################################################################################################################################################################################33

# Python3 program to reverse the 
# number using a stack 
#  
st = [] 
def push_digits(number): 

	while (number != 0): 
		st.append(number % 10)
		number = int(number / 10)

def reverse_number(number): 
	push_digits(number) 
	
	reverse = 0 
	i = 1 
	while (len(st) > 0): 
		reverse = reverse + (st[len(st) - 1] * i) 
		st.pop() 
		i = i * 10 
	return reverse 

number = 39997
print(reverse_number(number)) 

###################################################################################################################################################################################

#largest rectangular area in a histogram

def maxArea(histogram):
    stack=[]
    max_area=0
    i=0

    while i<len(histogram):
        if not stack or histogram[stack[-1]]<=histogram[i]:
            stack.append(i)
            i+=1
        else:
            top=stack.pop()
            area=histogram[top]*((i-stack[-1]-1)if stack else i)

            max_area=max(area,max_area)
    while stack: 
          
        top = stack.pop() 

        area = (histogram[top] * 
              ((i - stack[-1] - 1)  
                if stack else i)) 
  
        max_area = max(max_area, area) 
    return max_area 

hist = [6, 2, 5, 4, 5, 1, 6] 
print("Maximum area is",  
       maxArea(hist)) 

#######################################################################################################################################################################################3

class Node():
    def __init__(self,data):
        self.data = data
        self.left=self.right=None

def zigzag(root):
    if not root:
        return None
    curr=[]
    next=[]
    ltr=True
    curr.append(root)

    while len(curr)>0:
        temp=curr.pop()
        print(temp.data," ",end="")

        if ltr:
            if temp.left:
                next.append(temp.left)
            if temp.right:
                next.append(temp.right)
        else:
            if temp.right:
                next.append(temp.right)
            if temp.left:
                next.append(temp.left)
        if len(curr)==0:
            ltr= not ltr

            curr ,next = next,curr
            #swape these 

root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(7) 
root.left.right = Node(6) 
root.right.left = Node(5) 
root.right.right = Node(4) 
print("Zigzag Order traversal of binary tree is") 
zigzag(root) 

##################################################################################################################################################################################f

from queue import Queue

def generate(n):
    q=Queue()
    q.put("1")

    while n>0:
        n-=1
        s1=q.get()
        print(s1)
        s2=s1

        q.put(s1+"0")
        q.put(s2+"1")

n=10
generate(n)
######################################################################################################################################################################################

#geneate smallest multiple of n made from 0 and 9
 
from queue import Queue 

def generateNumbersUtil(): 
	global vec 

	q = Queue() 

	q.put("9") 
	for count in range(MAX_COUNT, -1, -1): 
		s1 = q.queue[0] 
		q.get() 
		
		vec.append(s1) 
		
		s2 = s1 
		s1 += "0"
		q.put(s1) 
		
		s2 += "9"
		q.put(s2) 

def findSmallestMultiple(n): 
	global vec 
 
	for i in range(len(vec)): 
		if (int(vec[i]) % n == 0): 
			return vec[i] 

MAX_COUNT = 10000 
vec = [] 
generateNumbersUtil()	 
n = 10	
print(findSmallestMultiple(n)) 
##########################################################################################################################################################################################3

