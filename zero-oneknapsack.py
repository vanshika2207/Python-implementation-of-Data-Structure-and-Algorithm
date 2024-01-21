class items:
    def __init__(self,profit,weight):
        self.profit=profit
        self.weight=weight
def knapsack(items,capacity,currentindex):
    tempdict={}
    dictkey=str(currentindex)+str(capacity)
    if capacity<=0 or currentindex<0 or currentindex>=len(items):
        return 0
    elif dictkey in tempdict:
        return tempdict[dictkey]
    elif items[currentindex].weight<=capacity:
        profit1=items[currentindex].profit+knapsack(items,capacity-items[currentindex].weight,currentindex+1)
        profit2=knapsack(items,capacity,currentindex+1)
        tempdict[dictkey] = max(profit1,profit2)
        return tempdict[dictkey]
    else:
        return 0
mango=items(31,3)
apple=items(26,1)
orange=items(17,2)
bannana=items(72,5)
item=[mango,apple,orange,bannana]
print(knapsack(item,7,0))