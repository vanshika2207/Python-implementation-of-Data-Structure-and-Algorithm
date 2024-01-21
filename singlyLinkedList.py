#creation
# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None
# class SlinkedList:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#     #for displaying the linked list
#     def __iter__(self):
#         node=self.head
#         while node:
#             yield node
#             node=node.next
# singlylinkedlist=SlinkedList()
# print([node.value for node in singlylinkedlist])
# node1=Node(1)
# node2=Node(2)
# print([node.value for node in singlylinkedlist])
# #now we will need to link the node with the head and tail
# #assign first node to the head of this linked list
# singlylinkedlist.head=node1
# singlylinkedlist.head.next=node2
# singlylinkedlist.tail=node2
#print([node.value for node in singlylinkedlist])
#insertion
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class SlinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    #for displaying the linked list
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insertion(self,value,location):
        newNode=Node(value)#creating new node
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            if location==0:
                newNode.next=self.head
                self.head=newNode
            elif location ==-1:
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                nextnode=tempNode.next
                tempNode.next=newNode
                newNode.next=nextnode
    def traverse(self):
        if self.head is None:
            print('singly linked list does not exist')
        else:
            tempvalue=self.head
            while tempvalue  is not None:
                print(tempvalue.value)
                tempvalue=tempvalue.next
    def search(self,nodeV):
        if self.head is None:
            return 'list does not exist'
        else:
            node=self.head
            while node is not None:
                if node.value==nodeV:
                    return node.value
                node=node.next
            return 'value does not exist'
    def delete(self,location):
        if self.head is None:
            return 'linked list does not exist'
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
            elif location==-1:
                 if self.head==self.tail:
                    self.head=None
                    self.tail=None
                 else:
                     node=self.head
                     while node is not None:
                         if node.next==self.tail:
                             break
                         node=node.next
                     node.next=None
                     self.tail=node
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index=+1
                nextnode=tempnode.next
                tempnode.next= nextnode.next

    def deleteentire(self):
        if self.head is None:
            print('the singly linked list does not exist')
        else:
            self.head=None
            self.tail=None



singlylinkedlist=SlinkedList()
singlylinkedlist.traverse()
singlylinkedlist.insertion(1,8)
singlylinkedlist.insertion(2,-1)
singlylinkedlist.insertion(5,1)
print([node.value for node in singlylinkedlist])
singlylinkedlist.traverse()
print(singlylinkedlist.search(5))
print(singlylinkedlist.search(0))
print([node.value for node in singlylinkedlist])
singlylinkedlist.delete(0)
singlylinkedlist.deleteentire()
print([node.value for node in singlylinkedlist])