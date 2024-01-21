activities=[['a',0,6],['b',3,4],['c',1,2],['d',5,8],['e',5,7],['f',8,9]]
def printmax(acitivities):
    acitivities.sort(key=lambda x:x[2])
    i=0
    firsta=acitivities[i][0]
    print(firsta)
    for j in range(len(acitivities)):
        if activities[j][1]>activities[i][2]:
            print(acitivities[j][0])
            i=j
printmax(activities)