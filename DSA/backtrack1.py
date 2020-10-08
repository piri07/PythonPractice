#prime number after number p and before sum s
set=[]
prime=[]
def isPrime(x):
    sqroot = int(x**0.5)
    flag = True

    if x==1:
        return False
    for i in range(2,sqroot+1):
        if x%i==0:
            return False
    return True

def display():
    global set,prime 
    lenn = len(set)
    for i in range(lenn):
        print(set[i],end=" ")
    print()

def primeSum(total,n,s,i):
    global set,prime
     
    if total==s and len(set)==n:
        display()
        return
    if total>s or i==len(prime):
        return
    
    set.append(prime[i])
    primeSum(total+prime[i],n,s,i+1)
    set.pop()
    primeSum(total,n,s,i+1)

def allPrime(n,s,p):
    global set,prime

    for i in range(p+1,s+1):
        if isPrime(i)==True:
            prime.append(i)

    if len(prime)<n:
        return
    primeSum(0,n,s,0)

S = 54
N = 4
P = 3
allPrime(N, S, P)


################################################################################################################################################################################33

#find all subsets 
def subsetsUtil(A,subset,i):
    print(*subset)
    for i in range(i,len(A)):
        subset.append(A[i])

        subsetsUtil(A,subset,i+1)

        subset.pop(-1)

    return

def subsett(A):
    subset=[]

    subsetsUtil(A,subset,0)

array = [1, 2, 3]   
subsett(array) 

#################################################################################################################################################################################3
#power set lexiographic order

def permuteRec(string, n, index = -1, curr = ""): 

	if index == n: 
		return

	if len(curr) > 0: 
		print(curr) 

	for i in range(index + 1, n): 
		curr += string[i] 
		permuteRec(string, n, i, curr) 

		curr = curr[:len(curr) - 1] 

def powerSet(string): 
	string = ''.join(sorted(string)) 
	permuteRec(string, len(string)) 

if __name__ == "__main__": 
	string = "cab"
	powerSet(string) 


