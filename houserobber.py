def houserobber(houses,currentindex):
    if currentindex>=len(houses):
        return 0
    else:
        stealfirst=houses[currentindex]+houserobber(houses,currentindex+2)
        skipfirst=houserobber(houses,currentindex+1)
        return max(stealfirst,skipfirst)
houses=(6,7,1,30,8,2,4)
print(houserobber(houses,0))

## using dynamic programming
#using memoization
def houserobbermemo(currentindex,houses):
    temp={}
    if currentindex>=len(houses):
        return 0
    if not currentindex in temp:
        stealfirst=houses[currentindex]+houserobbermemo(currentindex+2,houses)
        skipfirst=houserobbermemo(currentindex+1,houses)
        temp[currentindex]=  max(stealfirst,skipfirst)
    return temp[currentindex]
print(houserobbermemo(0,houses))

#using tabulation
def houserobbertab(houses):
    temp=[0]*(len(houses)+2)
    for i in range(len(houses)-1,-1,-1):
        temp[i]=max(houses[i]+temp[i+2],temp[i+1])
    return temp[0]
print(houserobbertab(houses))