#half pyramid using '*'
rows=5
#rows=int(input('enter number of rows"))
for i in range(rows):
    for j in range(i+1):
        print('*',end=' ')
    print('')
#half pyramid using numbers
for i in range(rows):
    for j in range(i+1):
        print(i,end=' ')
    print('')
for i in range(rows):
    for j in range(i+1):
        print(j,end=' ')
    print('')
#half pyramid using alphabets
asci=65
for i in range(rows):
    for j in range(i+1):
        print(chr(asci),end=' ')
        asci+=1
    print('')
asci2=97
for i in range(rows+1):
    for j in range(i+1):
        print(chr(asci2),end=' ')
    asci2+=1
    print()
#inverted half pyramid
for i in  range(rows,0,-1):
    for j in range(0,i):
        print('*',end=' ')
    print('')
for i in range(rows,0,-1):
    for j in range(0,i):
        print(i,end=' ')
    print('')
for i in range(rows,0,-1):
    for j in range(0,i):
        print(j+1,end=' ')
    print('')
#joining two pyramids -half diamond
n=int(input('enter number of rows'))
if n%2==0:
    for i in range(n//2):
        for j in range(i+1):
            print('*',end=' ')
        print('')

    for i in range(n//2,0,-1):
        for j in range(0,i):
            print('*',end=' ')
        print('')
else:
    for i in range(n//2):
        for j in range(i+1):
            print('*',end=' ')
        print('')
    print('* '*((n//2)+1))
    for i in range(n//2,0,-1):
        for j in range(0,i):
            print('*',end=' ')

        print('')
#full pyramid
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows + 1):
    for space in range(1, (rows - i) + 1):
        print(end="  ")

    while k != (2 * i - 1):
        print("* ", end="")
        k += 1

    k = 0
    print()
k=0
for i in range(1,rows+1):
    for space in range(1,(rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print(k,'',end='')
        k+=1
    k=0
    print()
#inverted full pyramid
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print(' ', end='')  # printing space and staying in same line

    for j in range(2 * i - 1):
        print('*', end='')  # printing * and staying in same line
    print()  # printing new line
##diamond
rows=int(input('enter number of rows'))
k=0
a=rows//2
for i in range(1,a+1):
    for space in range (1,(a-i)+1):
        print(' ',end='')
    while k!=(2*i-1):
        print('*',end='')
        k+=1
    k=0
    print()
for i in range(a,0,-1):
    for space in range(a-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')


    print()
print()


#hour glass
for i in range(a,0,-1):
    for space in range(a-i):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()
for i in range(1,a+1):
    for space in range(1,(a-i)+1):
        print(' ',end='')
    for j in range(2*i-1):
        print('*',end='')
    print()

for i in range(a,0,-1):
    for space in range(a-i):
        print(' ',end='')
    for j in range(2*i-1):
        print(i,end='')
    print()
for i in range(1,a+1):
    for space in range(1,(a-i)+1):
        print(' ',end='')
    for j in range(2*i-1):
        print(i,end='')
    print()
##pascal triangle
print()
print()
coef=1
rows=int(input('enter number of rows '))
for i in range(1,rows+1):
    for space in range(1,rows-i+1):
        print(' ',end='')
    for j in range(0,i):
        if j==0 or i==0:
            coef=1
        else:
            coef=coef*(i-j)//j
        print(coef,end=' ')
    print('')
##floyd triangle
s=1
for i in range(rows):
    for j in range(i+1):
        print(s,end='')
        s+=1
    print()