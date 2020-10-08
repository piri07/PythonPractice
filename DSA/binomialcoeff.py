# A Dynamic Programming based Python Program that uses table C[][] 
# to calculate the Binomial Coefficient 

# Returns value of Binomial Coefficient C(n, k) 
def binomialCoef(n, k): 
	C = [[0 for x in range(k+1)] for x in range(n+1)] 

	# Calculate value of Binomial Coefficient in bottom up manner 
	for i in range(n+1): 
		for j in range(min(i, k)+1): 
			# Base Cases 
			if j == 0 or j == i: 
				C[i][j] = 1

			# Calculate value using previously stored values 
			else: 
				C[i][j] = C[i-1][j-1] + C[i-1][j] 

	return C[n][k] 

# Driver program to test above function 
n = 5
k = 2
print("Value of C[" + str(n) + "][" + str(k) + "] is "
	+ str(binomialCoef(n,k))) 


#now by using memoization


def binomialCoeffUtil(n, k, dp): 
	
	# If value in lookup table then return 
	if dp[n][k] != -1: 
		return dp[n][k] 

	# Store value in a table before return 
	if k == 0: 
		dp[n][k] = 1
		return dp[n][k] 
	
	# Store value in table before return 
	if k == n: 
		dp[n][k] = 1
		return dp[n][k] 
	
	# Save value in lookup table before return 
	dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) +
				binomialCoeffUtil(n - 1, k, dp)) 
				
	return dp[n][k] 

def binomialCoeff(n, k): 
	
	# Make a temporary lookup table 
	dp = [ [ -1 for y in range(k + 1) ] 
				for x in range(n + 1) ] 

	return binomialCoeffUtil(n, k, dp) 

# Driver code 
n = 5
k = 2

print("Value of C(" + str(n) +
			", " + str(k) + ") is", 
			binomialCoeff(n, k)) 



