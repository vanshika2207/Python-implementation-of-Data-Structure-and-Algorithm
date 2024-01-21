def findlps(s,startindex,endindex):
    if startindex>endindex:
        return 0
    if s[startindex]==s[endindex]:
        return 2+findlps(s,startindex+1,endindex+1)
    else:
        op1=findlps(s,startindex,endindex-1)
        op2=findlps(s,startindex+1,endindex)
        return max(op1,op2)
print(findlps('elrmenmet',0,8))