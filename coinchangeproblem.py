def coinchange(totalnumber,coins):
   n=totalnumber
   coins.sort()
   index=len(coins)-1
   while True:
       coinvalue=coins[index]
       if n>=coinvalue:
           print(coinvalue)
           n=n-coinvalue
       if n<coinvalue:
           index-=1
       if n==0:
           break
coins=[1,2,5,20,50,100]
#coinchange(8,coins)
##dynamic approach
def dynamic(totalnumber,coins):
    dp=[float('inf')]*(totalnumber+1)
    dp[0]=0
    for i in range(1,totalnumber+1):
        for coin in coins:
            if coin<=i:
                dp[i]=min(dp[i],1+dp[i-coin])
    if dp[totalnumber] ==float('inf'):
        return -1
    return dp[totalnumber]

print(dynamic(8,coins))