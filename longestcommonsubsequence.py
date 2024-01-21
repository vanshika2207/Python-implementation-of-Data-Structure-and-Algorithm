def findlcs(s1,s2,index1,index2):
    if index1==len(s1) or index2==len(s2):
        return 0
    if s1[index1]==s2[index2]:
        return 1+findlcs(s1,s2,index1+1,index2+1)
    else:
        op1=findlcs(s1,s2,index1,index2+1)
        op2=findlcs(s1,s2,index1+1,index2)
        return max(op1,op2)
print(findlcs('elephant','eliohat',0,0))


def longestCommonSubsequence( text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    m = len(text1)
    n = len(text2)
    t = [[0] * (n + 1) for i in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                t[i][j] = t[i - 1][j - 1] + 1
            else:
                t[i][j] = max(t[i][j - 1], t[i - 1][j])

    return  t[m][n]
    s = ""
    while m > 0 and n > 0:
        if text1[m - 1] == text2[n - 1]:
            s += text1[m - 1]
            m -= 1
            n -= 1
        elif t[m - 1][n] > t[m][n - 1]:
            m -= 1
        else:
            n -= 1

    return s[::-1]
print(longestCommonSubsequence('elephant','eliohat'))