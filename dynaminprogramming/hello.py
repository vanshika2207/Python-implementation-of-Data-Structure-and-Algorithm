#fibonacci with recurssion
def fib(n):
    if  n==1:
        return 0
    if n==2:
        return 1

    else:
        return fib(n-1)+fib(n-2)
print(fib(6)) #0 1 1 2 3
#fibonacci using memoization
def fibmemo(n):
    if n==1 :
        return 0
    if n==2:
        return 1
    memo={}
    if not n in memo:
        memo[n]=fib(n-1)+fib(n-2)
    return memo[n]
print(fibmemo(6))
#fibonacci using tabulation
def fibtab(n):
    tb=[0,1]
    for i in range(2,n+1):
        tb.append(tb[i-1]+tb[i-2])
    return  tb[n-1]
print(fibtab(6))

