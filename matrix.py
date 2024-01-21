#add two matrix
a=[[1,2,3],
   [3,6,9]]
b=[[3,4,6],
   [7,8,9]]
result=[[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j]=a[i][j]+b[i][j]
for r in result :
    print(r)

# list comprehension
result=[[a[x][y]+b[x][y] for x in range(len(a))]for y in range(len(a[0]))]
print(result)
result=[[0,0],[0,0],[0,0]]
##transpose of matrix
for i in range(len(a)):
    for j in range(len(a[i])):
        result[j][i]=a[i][j]
for r in result:
    print(r)
##    list comprehension
result=[[a[j][i] for j in range (len(a))]for i in range (len(a[0]))]
print(result)
##creating the matrix from the user input
row=int(input('enter the number of rows'))
col=int(input('enter the number of columns'))
matrix=[]
for i in range(row):
    a=[]
    for j in range(col):
        a.append(int(input()))
    matrix.append(a)
for i in range(row):
    for j in range(col):
        print(matrix[i][j],end='')
    print()

# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]+=X[i][k]*Y[k][j]
for r in result:
    print(r)
def gridchallenge(grid):
    n=len(grid)
    m=len(grid[0])
    grid[0]=sorted(grid[0])
    for i in range(n):
        grid[i]=sorted(grid[i])
        for j in range(m):
            if grid[i-1][j]>grid[i][j]:
                return('No')
    return('yES')
a=gridchallenge(['mpxz','abcd' ,'wlmf'])
print(a)
