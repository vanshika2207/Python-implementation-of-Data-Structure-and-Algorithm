#recursion
#tail
def my_func(n):
    if(n>0):
        print(n,end=' ')
        my_func(n-1)
my_func(4)
print()
#head
def my_func2(n):
    if(n>0):
        my_func2(n-1)
        print(n,end=' ')
my_func2(4)
print()
#tree
def my_func3(n):
    if(n>0):
        print(n,end=' ')
        my_func3(n-1)
        my_func3(n-1)
my_func3(4)
print()
#nested
def my_func4(n):
    if (n>100):
        return n-10
    else:
        return(my_func4(my_func4(n+11)))
print(my_func4(95))
#in direct
def func_A(n):
    if n > 0:
        print(n, end=" ")
        func_B(n - 1)  # calling func_B


def func_B(n):
    if n > 0:
        print(n, end=" ")
        func_C(n - 1)  # calling func_C


def func_C(n):
    if n > 0:
        print(n, end=" ")
        func_A(n // 2)  # calling func_A


func_A(20)
print()
#fibonacci series
def f(n):
    if n<0 or int(n)!=n:
        print("sorry")
    elif n==0 or n==1:
        return n
    else:
        return f(n-1)+f(n-2)

print(f(4))
#sum_of_digit_of_number
def s(n):
    if n<0 or int(n)!=n:
        return "undefine"
    elif n==0:
        return 0
    else:
        return n%10+s(n//10)
print(s(3214))
#power of a number
def p(b,e):
    if e<0 or int(e)!=e:
        return 'power should be positive'
    elif e==0:
        return 1
    else:
        return b*p(b,e-1)
print(p(3,4))
#gcd of two number
def gcd(a,b):
    if int(a)!=a or int(b)!=b:
        return 'not define'
    if a<0:
        a=-a
    if b<0:
        b=-b
    if b==0:
        return a
    else:
        hcf= gcd(b,a%b)
        print(f'{a} and {b} hcf is',hcf)
    lcm=(a*b)//hcf
    print(f'{a} and {b} lcm is', lcm)
print(gcd(60,36))
print(gcd(36,60))
print(gcd(60,-36))
print(gcd(60.90,36))
#converting decimal to binary number
def db(n):
    if int(n)!=n:
        return ' undefined'
    elif n==0:
        return 0
    else :
        return n%2+10*db(n//2)
a=db(10)
print(a)