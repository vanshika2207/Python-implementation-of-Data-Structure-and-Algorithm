def findmincost(twodarray,row,col):
    if row==-1 or col==-1:
        return float('inf')
    if row==0 and col==0:
        return  twodarray[row][col]
    else:
        op1=findmincost(twodarray,row-1,col)
        op2=findmincost(twodarray,row,col-1)
        return twodarray[row][col]+min(op1,op2)
a=[[4,7,8,6,4],[6,7,3,9,2],[3,8,1,2,4],[7,1,7,3,7],[2,9,8,9,3]]
print(findmincost(a,4,4))

def numberofpaths(twodarray,row,col,cost):
    if cost<0:
        return 0
    elif row==0 and col==0:
        if twodarray[0][0]-cost==0:
            return 1
        else:
            return 0
    elif row==0:
        return numberofpaths(twodarray,0,col-1,cost-twodarray[row][col])
    elif col==0:
        return numberofpaths(twodarray,row-1,0,cost-twodarray[row][col])
    else:
        op1=numberofpaths(twodarray,row-1,col,cost-twodarray[row][col])
        op2=numberofpaths(twodarray,row,col-1,cost-twodarray[row][col])
        return op1+op2
print(numberofpaths(a,3,3,25))