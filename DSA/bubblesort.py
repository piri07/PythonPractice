def bubble(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j] , array[j+1] = arr[j+1],array[j]


arr=[-2,0,45,8,-9,63]

bubble(arr)
print(arr)