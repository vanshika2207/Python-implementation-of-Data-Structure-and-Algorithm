# # # # #stack creation using list without size limit
# # # # class Stack:
# # # #     def __init__(self):
# # # #         self.list=[]
# # # #     def __str__(self):
# # # #         values=self.list.reverse()
# # # #         values=[str(x) for x in self.list]
# # # #         return '\n'.join(values)
# # # #
# # # #     def isEmpty(self):
# # # #         if self.list==[]:
# # # #             return True
# # # #         else:
# # # #             return False
# # # #     def push(self,value):
# # # #         self.list.append(value)
# # # #         return 'the element has been successfully added to the stack'
# # # #     def pop(self):
# # # #         if self.isEmpty():
# # # #             return 'the stack is empty'
# # # #         else:
# # # #             return self.list.pop()
# # # #     def peek(self):
# # # #         if self.isEmpty():
# # # #             return 'the stack is empty'
# # # #         else:
# # # #             return self.list[0]
# # # #     def delete(self):
# # # #         self.list=None
# # # #
# # # #
# # # #
# # # # st=Stack()
# # # # st.isEmpty()
# # # # st.push(1)
# # # # st.push(2)
# # # # st.push(3)
# # # # st.delete()
# # # #
# # class Stack:
# #     def __init__(self,maxSize):
# #         self.maxSize=maxSize
# #         self.list=[]
# #     def __str__(self):
# #         values=self.list.reverse()
# #         values=[str(x) for x in self.list]
# #         return '\n'.join(values)
# #     def isFull(self):
# #         if len(self.list)==self.maxSize:
# #             return True
# #         else :
# #             return False
# #     def push(self,values):
# #         if self.isFull():
# #             return 'stack is full '
# #         else:
# #             self.list.append(values)
# #             print('value added successfully')
# #     def isEmpty(self):
# #         if self.list==[]:
# #             return True
# #         else:
# #             return False
# #     def pop(self):
# #         if self.isEmpty():
# #             return 'stack is empty'
# #         else:
# #             return self.list.pop()
# #     def delete(self):
# #         self.list=None
# #     def peek(self):
# #         if self.isEmpty():
# #             return 'stack is empty'
# #
# #         else:
# #             return self.list[len(self.list)-1]
# #     def minelement(self):
# #         return min(self.list)
# #
# #
# #
# # st=Stack(10)
# # print(st)
# # print(st.isEmpty())
# # print(st.isFull())
# # print(st.push(12))
# # print(st.push(34))
# # print(st.push(16))
# # st.push(25)
# # st.push(45)
# # st.pop()
# # st.push(0)
# # st.push(100)
# # print(st.pop())
# # print(st.peek())
# # print(st.minelement())
# #
# # #
# # #
# # #
# # ##implementation of stack using linked list
# # class Node:
# #     def __init__(self,value=None):
# #         self.value=value
# #         self.next=None
# #     def __str__(self):
# #         return str(self.value)
# # class LinkedList:
# #     def __init__(self):
# #         self.head=None
# #         self.tail=None
# #     def __iter__(self):
# #         node=self.head
# #         while node:
# #             yield node
# #             node=node.next
# # class Stack:
# #     def __init__(self):
# #         self.LinkedList=LinkedList()
# #     def __str__(self):
# #         values=[str(x.value) for  x in self.LinkedList]
# #         return '\n'.join(values)
# #     #if the head node is none then stack is empty
# #     def isEmpty(self):
# #         if self.LinkedList.head==None:
# #             return True
# #         else:
# #             return  False
# #     def push(self,value):
# #         new_node=Node(value)
# #         new_node.next=self.LinkedList.head
# #         self.LinkedList.head=new_node
# #
# #     def pop(self):
# #         if self.isEmpty():
# #             return'sorry'
# #         else:
# #             temp_node=self.LinkedList.head.value
# #             self.LinkedList.head=self.LinkedList.head.next
# #             return temp_node
# #     def peek(self):
# #         if self.isEmpty():
# #             return 'Sorry'
# #         else:
# #             temp_node=self.LinkedList.head.value
# #             return temp_node
# #     def delete(self):
# #         self.LinkedList.head=None
# # temp=Stack()
# # temp.push(1)
# # temp.push(2)
# # temp.push(3)
# # print(temp)
# # temp.pop()
# # print(temp.peek())
# #
# #
# # #tower of hanoi using recurssion
# # def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
# #     if n == 0:
# #         return
# #     TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
# #     print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
# #     TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)
# #
# #
# # # Driver code
# # N = 3
# #
# # # A, C, B are the name of rods
# # TowerOfHanoi(N, 'A', 'C', 'B')
# #
# # #design a data structure to inplement two stack using a single list
# #
# # class twoStack:
# #     def __init__(self,n):
# #         self.size=n
# #         self.arr=[None]*n
# #         self.top1=-1
# #         self.top2=self.size
# #
# #     def push1(self,x):
# #         if self.top1<self.top2-1:
# #             self.top1=self.top1+1
# #             self.arr[self.top1]=x
# #         else:
# #             print('Stack overflow')
# #     def push2(self,x):
# #         if self.top1<self.top2-1:
# #             self.top2=self.top2-1
# #             self.arr[self.top2]=x
# #         else:
# #             print('Stack overflow')
# #
# #     def pop1(self):
# #         if self.top1>=0:
# #             x=self.arr[self.top1]
# #             self.top1=self.top1-1
# #             print(x)
# #         else:
# #             print('stack underflow')
# #
# #     def pop2(self):
# #         if self.top2<self.size:
# #             x=self.arr[self.top1]
# #             self.top2=self.top1+1
# #             print(x)
# #         else:
# #             print('stack underflow')
# # # Driver program to test twoStacks class
# # ts = twoStack(5)
# # ts.push1(5)
# # ts.push2(10)
# # ts.push2(15)
# # ts.push1(11)
# # ts.push2(7)
# #
# # stacks=[8]
# #
# #
# #
# class stack:
#     def __init__(self,n):
#         self.items=[0]*n
#         self.n=n
#         self.top=-1
#     def __str__(self):
#         #self.items.reverse()
#         values=[str(x) for x in self.items]
#         return ' '.join(values)
#     def isempty(self):
#         if self.top==-1:
#             return True
#         else:
#             False
#     def isfull(self):
#         if self.top==self.n-1:
#             return True
#         else:
#             return False
#     def push(self,val):
#         if self.isfull():
#             print('sory')
#         else:
#             self.top=self.top+1
#             self.items[self.top]=val
#     def pop(self):
#         if self.isempty():
#             print('sorry')
#         else:
#             temp=self.items[self.top]
#             self.top=self.top-1
#             return temp
#     def peek(self):
#         return self.items[self.top]
# st=stack(4)
# print(st.isempty())
# print(st.isfull())
# print(st.push(5))
# print(st.push(6))
# print(st.push(7))
# print(st.push(9))
# print(st)
# st.pop()
# print()
# print(st.pop())
# print(st.peek())

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()

    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        return '\n'.join(values)
    def isempty(self):
        if self.LinkedList.head==None:
            return True
        else:
            return False
    def push(self,value):
        new_node=Node(value)
        new_node.next=self.LinkedList.head
        self.LinkedList.head=new_node

    def pop(self):
        if self.isempty():
            return True
        else:
            temp=self.LinkedList.head.value
            self.LinkedList.head=self.LinkedList.head.next
            print(temp)
    def peek(self):
        if self.isempty():
            return True
        else:
            temp=self.LinkedList.head.value

            print(temp)
    def delete(self):
        self.LinkedList.head=None

s=Stack()
print(s.isempty())
s.push(34)
s.push(90)
s.push(31)
print(s)
s.pop()
s.peek()
