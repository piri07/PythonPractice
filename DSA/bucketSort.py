#The process of bucket sort can be understood as a scatter-gather approach. 
# The elements are first scattered into buckets then the elements of buckets are sorted. 
# Finally, the elements are gathered in order.


def bucketSort(arr):
    bucket=[]

    for i in range(len(arr)):
        bucket.append([])

    for j in arr:
        index_b = int(10*j)
        bucket[index_b].append(j)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])
    
    k=0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k+=1
    return arr

array = [.42, .32, .33, .52, .37, .47, .51]
print("Sorted Array in descending order is")
print(bucketSort(array))