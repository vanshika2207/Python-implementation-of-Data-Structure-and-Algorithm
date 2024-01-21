# # '''
# # #creating array
# # from array import *
# # #creating array of integer type
# # arr_1=array('i',[3,2,7,6,9])
# # print(arr_1)
# # #creating array of double type
# # arr_2=array('d',[1.7,8.9,9.0])
# # print(arr_2)
# # #getting user input for an array
# # arr_3=array('i',[])
# # n=int(input('enter length of the array :'))
# # for i in range(n):
# #     val=int(input("enter value :"))
# #     arr_3.append(val)
# # print("array :",arr_3)
# # for i in range(n):
# #     print(arr_3[i])
# #
# # #INSERTING ELEMENT IN THE ARRAY
# # ##using array
# # k=int(input('where you want to insert the element ?'))
# # element=int(input('enter the element you want to insert ?'))
# # arr_3.insert(k,element)
# # print(arr_3)
# # #deleting array element
# # delete=int(input('enter element you wnat to remove'))
# # arr_3.remove(delete)
# # print(arr_3)
# #
# # ##searching array element
# # ##using linear search
# # def search_ele(arr, key):
# #     for i in range(len(arr)):
# #         if arr[i] == key:
# #             return i         # returning the index val
# #     return "Element not found"
# #
# # #creating an array of integer data type
# # my_arr = array('i', [5, 3, 4, 8, 9])
# #
# # #searching for element 4
# # print(search_ele(my_arr, 4))
# # ##more operation
# # #append()
# # arr_3.append(12)
# # print(arr_3)
# # #extend() -add an iterable item at the end of the list
# # arr_3.extend(arr_1)
# # print(arr_3)
# #
# # #fromlist() takes a list as a parameter and adds all the item of the list at the end of the array
# # from array import *
# # my_arr=array('i',[5,3,4])
# # list1=[13,67]
# # my_arr.fromlist(list1)
# # print(my_arr)
# # #pop(<index>,by default=-1)
# # a=my_arr.pop()
# # print(a)
# # #index()-RETURN THE FIRST OCCURENCE OF THE ITEM
# # my_arr = array('i', [5, 3, 4, 15])
# #
# # #Getting the index of item 15
# # ind = my_arr.index(15)
# # print("Index val of element 15: ", ind)
# # #REVERSE()
# # my_arr.reverse()
# # print(my_arr)
# # #buffer_info() returns the current memory adddress and the length of the array in a tuple format
# # print(my_arr.buffer_info())
# # #count()
# # b=my_arr.count(15)
# # print(b)
# # #tolist()-convert array to the list
# # c=my_arr.tolist()
# # print(c)
# # print(type(c))
# # #performing array operation
# # array=array('l',[0,1,2,3,4,5,6,7,8,9])
# # print(array[:])
# # print(array[0:9])
# # print(array[0:3])
# # print(array[1:9])
# # print(array[-1:])
# # print(array[-1:-5])
# # print(array[-5:-1])
# # print(array[-2:])
# # print(array[-2:2])
# # print(array[-2:-3])
# #
# # #to find max element and its position in array
# # from array import *
# # n=int(input('enter max number of element in array ?'))
# # a=array('i',[])
# # for i in range(n):
# #     val=int(input('enter array element'))
# #     a.append(val)
# # print(a)
# # max=a[0]
# # pos=0
# # for i in range(0,len(a)):
# #     if max<a[i]:
# #         max=a[i]
# #         pos=i
# # print('maximum element is ',max,'at',pos+1)
# #
# #
# # #create a two dimensional array
# # from numpy import *
# # arr_name=array([[4,3,5,6],[5,3,5,9]])
# # print(arr_name)
# # #creating a 3d array
# # arr_name=array([[[2,30],[3,60]]])
# # print(arr_name)
# # #creating 2-D array
# # m=int(input('enter number of rows'))
# # n=int(input('enter number of columns'))
# # a=[[input() for x in range(n)] for x in range(m)]
# # print(a)
# #
# # import numpy as np
# # a=np.array([[2,3,4],[7,8,9]])
# # ## inserting the element
# # #using the np.insert(array,index,values,,axis)
# # ###axis=1 adding column ,axis=0 adding roe
# # b=np.array([10,11])
# # c=np.insert(a,0,b,axis=1)
# # print(c)
# # d=np.array([89,32,56])
# # e=np.insert(a,2,d,axis=0)
# # print(e)
# # #using append()
# # f=np.array([[1,2,7],[8,9,0],[5,6,3]])
# # g=np.append(f,d)
# # print(g)
# # for i in range(len(f)):
# #     for j in range (len(f[0])):
# #         print(f[i][j],end=' ')
# #     print()
# # m=3
# # n=3
# # matrix=[]
# # print('enter the entries row wise')
# # #for user input
# # for i in range(m):
# #     a=[]
# #     for j in range(n):
# #         a.append(int(input()))
# #     matrix.append(a)
# # #for printing
# # for i in range(m):
# #     for j in range(n):
# #         print(matrix[i][j],end=' ')
# #     print()
# # r=int(input('enter number of rows '))
# # c=int(input('enter number of columns'))
# # matrix=[]
# # for i in range(r):
# #     a=[]
# #     for j in range(c):
# #         a.append(int(input(f'enter[{i}][{j}]')))
# #     matrix.append(a)
# # print('the given matrix is :')
# # for i in range(r):
# #     for j in range(c):
# #         print(matrix[i][j],end=' ')
# #     print()
# # element=int(input('enter element you want to search from the array'))
# # for i in range(r):
# #     for j in range(c):
# #         if matrix[i][j]==element:
# #             print('found ',i,j)
# #
# # #removing element
# # ## use delete(array,index,axis=1 from col)
# # from numpy import *
# # arr_1 = array([[4, 5, 6], [5, 3, 2], [7, 0, 4]])
# # print(arr_1)
# # arr_2 = delete(arr_1, 1, axis = 1)
# # print(arr_2)
# # ##mapping two arrays
# # arr1=[0,0,1,2,3]
# # arr2=[4,4,6,8,7]
# # map12=dict(zip(arr1,arr2))
# # print(map12)
# # ##shuffle array in python
# # import random
# # mylist=[2,3,4,4]
# # a=random.choice(mylist)
# # print(a)
# # b=random.sample(mylist,3)
# # print(b)
# # random.shuffle(mylist)
# # print(mylist)
# # #sliding window in array
# # ##The window sliding algorithm is used to find the maximum sum of elements in the array taking a given number of elements as fixed in one iteration.
# # ## The length of the array should be greater than the fixed length. In the following code, in each iteration, the sum can be calculated by removing
# # # the leftmost element and adding the rightmost element to w_sum.
# # def maxSum(arr,k):
# #     n=len(arr)
# #     if n<k:
# #         print('invalid')
# #         return -1
# #     #sum of first window of size k
# #     w_sum=sum(arr[:k])
# #     #first sum computed
# #     max_sum=w_sum
# #     for i in range(n-k):
# #         w_sum=w_sum-arr[i]+arr[i+k]
# #         max_sum=max(w_sum,max_sum)
# #     return max_sum
# #
# # # main code
# # arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
# # k = 4
# # print(maxSum(arr, k))
# # a=[]
# # n=int(input())
# # i=0
# # while i <0:
# #     a.append(int(input()))
# #     print(a)
# # '''
# # ##combine two array remove overlapping value
# # a=[1,2,3,4]
# # b=[1,2,5,6]
# # for i in b:
# #     if i not in a:
# #         a.append(i)
# # print(a)
# # ##covarience of two array:
# # def covar(x,y):
# #     mean_x=sum(x)/float(len(x))
# #     mean_y=sum(y)/float(len(y))
# #     sub_x=[i-mean_x for i in x]
# #     sub_y=[i-mean_y for i in y]
# #     numerator=sum([sub_x[i]*sub_y[i] for i in range(len(sub_x))])
# #     denominator=len(x)-1
# #     cov=numerator/denominator
# #     return cov
# # x = [12,45,23,58]
# # y = [52,1,35,89]
# # cov = covar(x, y)
# # print("Covariance of x and y :", cov)
# # #intersection between two arrays in python
# # a=[1,2,3,4,5]
# # b=[4,5,6,7,8]
# # c=list(filter(lambda x: x in a,b))
# # print(len(c))
#
# #create an array and traverse it
# a=[45,23,56]
# for i in a:
#     print(i)
# #accessing individual element through indexes
# # def access(array,index):
# #     if index>len(array):
# #         print('out of index')
# #     else:
# #         print(array[index])
# # access(a,2)
# # #append any value in the array using append() method
# # a.append(int(input('enter value')))
# # print(a)
# # #insert value in the array using insert method
# # i=int(input('enter index'))
# # v=int(input('enter value'))
# # a.insert(i,v)
# # print(a)
# # #extend python array using extend() method
# # new=eval(input('enter list'))
# # a.extend(new)
# # print(a)
# #add items from list into array using fromlist()
# import array as arr
# x=arr.array('i',[2,3,45,66])
# y=[34,12]
# x.fromlist(y)
# print(x)
# x.remove(66)
# print(x)
# x.pop()
# print(x)
# a=x.index(34)
# print('index is',a)
# x.reverse()
# print(x)
# a=x.buffer_info()
# print(a)
# b=x.count(34)
# print(b)
# c=x.tolist()
# print(x)
##multidimensional array
rows=int(input('enter row number'))
columns=int(input('enter column number'))
matrix=[]
for i in range((rows)):
    a=[]
    for j in range(columns):
        a.append(int(input('enter value')))
    matrix.append(a)
print(matrix)
##traversing
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end='')
    print()
##accessing element
i=int(input('enter row value'))
j=int(input('enter column value'))
print('the value is ',matrix[i][j])
import numpy as np
#inserting element
index=int(input('enter index'))
axis=int(input('enter axis 0 or 1'))

a=[1,2]
m=np.insert(matrix,index,a,axis)
print(m)

