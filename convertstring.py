def minoperations(s1,s2,m,n):

    if m==0:
        return n
    if n==0:
        return m
    if s1[m-1]==s2[n-1]:
        return minoperations(s1,s2,m-1,n-1)
    return 1+ min(minoperations(s1,s2,m,n-1),minoperations(s1,s2,m-1,n),minoperations(s1,s2,m-1,n-1))


print(minoperations('elephant','eliohat',8,7))
##using memoization
def minoperation2(s1,s2,index1,index2):
    tempdict={}
    if index1==len(s1):
        return len(s2)-index2
    if index2==len(s2):
        return len(s1)-index1
    if s1[index1]==s2[index2]:
        return minoperations(s1,s2,index1+1,index2+1)
    else:
        dictkey=str[index1]+str[index2]
        if dictkey not in tempdict:
            deleteop = 1 + minoperations(s1, s2, index1, index2 + 1)
            insertop = 1 + minoperations(s1, s2, index1 + 1, index2)
            replaceop = 1 + minoperations(s1, s2, index1 + 1, index2 + 1)
            tempdict[dictkey]= min(deleteop, insertop, replaceop)
        return tempdict[dictkey]
print(minoperation2('elephant','eliohat',0,0))


def minoperation(w1,w2):
    n=len(w1)
    m=len(w2)
    dp=[[0]*(m+1) for i in range(n+1) ]
    for i in range(n+1):
        dp[i][0]=i
    for j in range(m+1):
        dp[0][j]=j
    for i in range(1,n+1):
        for j in range(1,m+1):
            if w1[i-1]==w2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(
                    dp[i-1][j-1],
                    dp[i][j-1],
                    dp[i-1][j]
                )
    return dp[-1][-1]
print(minoperation('elephant','eliohat'))