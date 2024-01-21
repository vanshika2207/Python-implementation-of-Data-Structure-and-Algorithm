#number factor using divide and conquer
def numberfactor(n):
    if n in (0,1,2):
        return 1
    elif n==3:
        return 2
    else:
        subp1=numberfactor(n-1)
        subp2=numberfactor(n-3)
        subp3=numberfactor(n-4)
        return subp1+subp2+subp3
print(numberfactor(5))
##using dynamic programming
#memoization
def numberfactormemo(n):
    if n in (0,1,2):
        return 1
    if n==3 :
        return 2
    memo={}
    if not n in memo:
        sub1=numberfactor(n-1)
        sub2=numberfactor(n-3)
        sub3=numberfactor(n-4)
        memo[n]=sub1+sub2+sub3
    return memo[n]
print(numberfactormemo(5))
#tabulation
def numberfactab(number):
    dp=[1,1,1,2]
    for i in range(4,number+1):
        dp.append(dp[i-1]+dp[i-3]+dp[i-4])
    return dp[number]
print(numberfactab(5))