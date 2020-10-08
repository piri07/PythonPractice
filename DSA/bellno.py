def bellNumber(n):

    bell=[[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0]=1

    for i in range(1,n+1):
        #assign the first element of new row to be the last element of the previous row 
        bell[i][0] = bell[i-1][i-1]
        for j in range(n+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]


for n in range(80):
    print("bell number " ,n, "is" , bellNumber(n) )