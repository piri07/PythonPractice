#Given an array arr that is a permutation of [0, 1, ..., arr.length - 1], 
# we split the array into some number of "chunks" (partitions), and individually sort each chunk.  
# After concatenating them, the result equals the sorted array.


l=[1,0,2,3,4]
l1=sorted(l)

res=0
temp=0

for i in range(len(l)):
    temp = max(temp,l[i])
    if temp==l1[i]:
        res+=1
        c=0
print(res)