# #creation of queue without size limit
# class Queue:
#     def __init__(self):
#         self.items=[]
#     def __str__(self):
#         values=[str(x) for x in self.items]
#         return ' '.join(values)
#     def isEmpty(self):
#         if self.items==[]:
#             return True
#         else:
#             return False
#     def enqueue(self,value):
#         self.items.append(value)
#         return 'the element is succcessfully inserted at the end of the queue'
#     def dequeue(self):
#         if self.isEmpty():
#             return 'the queue does not exist'
#         else:
#             return self.items.pop(0)
#     def peek(self):
#         if self.isEmpty():
#             return 'the queue does not exist'
#         else:
#             return self.items[0]
#     def delete(self):
#         self.items=None
# q=Queue()
# print(q)
# print(q.isEmpty())
# q.enqueue(34)
# q.enqueue(45)
# q.enqueue(46)
# q.enqueue(90)
# q.enqueue(23)
# print(q)
# print(q.isEmpty())
# print(q.dequeue())
# print(q.dequeue())
# print(q)
# print(q.peek())
# q.delete()
##

#Queue with size limit
# class Queue:
#     def __init__(self,maxsize):
#         self.maxsize=maxsize
#         self.items=[]
#     def __str__(self):
#         values=[str(x) for x in self.items]
#         return ' '.join(values)
#     def isEmpty(self):
#         if self.items==[]:
#             return True
#         else :
#             return False
#     def isFull(self):
#         if len(self.items)==self.maxsize:
#             return True
#         else:
#             return False
#     def enqueue(self,value):
#         if self.isFull():
#             return 'sorry ,queue is full'
#         else:
#             return self.items.append(value)
#     def dequeue(self):
#         if self.isEmpty():
#             return 'sorry,queue is empty'
#         else:
#             return self.items.pop(0)
#     def peek(self):
#         if self.isEmpty():
#             return 'sorry ,queue is empty'
#         else:
#             return self.items[0]
#     def delete(self):
#         self.items=None
#         return 'deleted'
# q=Queue(5)
# q.enqueue(34)
# q.enqueue(56)
# q.enqueue(67)
# q.enqueue(90)
# q.enqueue(45)
# print(q)
# print(q.enqueue(560))
# q.dequeue()
# q.dequeue()
# print(q)
# #creation of queue using linked list
# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None
#     def __str__(self):
#         return str(self.value)
# class LinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     def __iter__(self):
#         current_node=self.head
#         while current_node:
#             yield current_node
#             current_node=current_node.next
# class queue:
#     def __init__(self):
#         self.LinkedList=LinkedList()
#     def __str__(self):
#         values=[str(x) for x in self.LinkedList]
#         return ' '.join(values)
#     def isempty(self):
#         if self.LinkedList.head==None:
#             return True
#         else:
#             return False
#     def enqueue(self,val):
#         new_node=Node(val)
#         if self.LinkedList.head==None:
#             self.LinkedList.head=new_node
#             self.LinkedList.tail=new_node
#         else:
#             self.LinkedList.tail.next=new_node
#             self.LinkedList.tail=new_node
#     def dequeue(self):
#         if self.isempty():
#             return'queue does not exist'
#         else:
#             temp_node=self.LinkedList.head.value
#             if self.LinkedList.head==self.LinkedList.tail:
#                 self.LinkedList.head=None
#                 self.LinkedList.tail=None
#             else:
#                 self.LinkedList.head=self.LinkedList.head.next
#             return temp_node
#
#     def peek(self):
#         if self.isEmpty():
#             return "The Queue does not exist."
#         else:
#             return self.LinkedList.head
#
#     def delete(self):
#         self.LinkedList.head = None
#         self.LinkedList.tail = None
#
# tempQueue = queue()
# tempQueue.enqueue(1)
# tempQueue.enqueue(2)
# tempQueue.enqueue(3)
# print(tempQueue)
# tempQueue.dequeue()
# print(tempQueue)
# class linearq:
#     def __init__(self,n):
#         self.item=[0]*n
#         self.n=n
#         self.front=-1
#         self.rear=-1
#     def __str__(self):
#         value=[str(x) for x in self.item]
#         return ' '.join(value)
#     def isFull(self):
#         if self.rear==self.n-1:
#             return True
#         else:
#             return False
#     def isempty(self):
#         if self.front<0 or self.front>self.rear:
#             return True
#         else :
#             return False
#
#     def enqueue(self,val):
#         if self.isFull():
#             print('sorry')
#         elif self.front==-1 and self.rear==-1:
#             self.front=0
#             self.rear=0
#             self.item[self.rear] = val
#         else:
#             self.rear=self.rear+1
#             self.item[self.rear]=val
#             print('success')
#     def dequeue(self):
#         if self.isempty():
#             return False
#         temp = self.item[self.front]
#         if (self.front==self.rear) and self.rear!=-1:
#             self.front=-1
#             self.rear=-1
#         else:
#             self.front=self.front+1
#         print('success')
#         return temp
#     def peek(self):
#         return self.item[self.front]
#
# lq=linearq(5)
# print(lq.isempty())
# print(lq.isFull())
# lq.enqueue(1)
# lq.enqueue(4)
# lq.enqueue(5)
# lq.enqueue(6)
# lq.enqueue(2)
# print(lq)
# lq.enqueue(8)
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.dequeue())
# print(lq.dequeue())
# lq.enqueue(90)
# print(lq.peek())

class Circularq:
    def __init__(self,n):
        self.items=[0]*n
        self.n=n
        self.rear=-1
        self.front=-1
    def __str__(self):
        values=[str(x) for x in self.items]
        return ' '.join(values)
    def isfull(self):
        if (self.front==0 and self.rear==self.n-1) or self.front==self.rear+1:
            return True
        else:
            return False
    def isempty(self):
        if self.front==-1:
            return True
        else:
            return False
    def enqueue(self,val):
        if self.isfull():
            return  'Soory'
        elif self.front==-1 and self.rear==-1:
            self.front=0
            self.rear=0
            self.items[self.rear]=val
        elif self.rear ==self.n-1:
            self.rear=0
            self.items[self.rear] = val
        else:
            self.rear=self.rear+1
            self.items[self.rear] =val

    def dequeue(self):
        if self.isempty():
            return 'Sorry'
        temp=self.items[self.front]
        if self.rear== self.front and self.front!=-1:
            self.rear=-1
            self.front=-1
        elif self.front==self.n-1:
            self.front=0
        else:
            self.front=self.front+1
        return temp
    def peek(self):
        return self.items[self.front]


cq=Circularq(5)
print(cq.isfull())
print(cq.isempty())
cq.enqueue(23)
cq.enqueue(56)
cq.enqueue(67)
cq.enqueue(89)
cq.enqueue(70)
cq.enqueue(78)

print(cq)
cq.dequeue()
cq.dequeue()
cq.enqueue(78)
cq.enqueue(59)
cq.enqueue(64)
cq.dequeue()
cq.enqueue(64)
print(cq)
print(cq.peek())