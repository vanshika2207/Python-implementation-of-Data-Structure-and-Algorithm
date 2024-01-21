#creating doubly linked list
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def creation(self,nodevalue):
        node=Node(nodevalue)
        node.prev=None
        node.next=None
        self.tail=node
        self.head=node
        print('created')
    def insertion(self,nodeValue,location):
        if self.head is None:
            print('the node canot be inserted')
        else:
            newNode=Node(nodeValue)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            elif location==-1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode
            else:
                index=0
                tempvalue=self.head
                while index<location-1:
                    tempvalue=tempvalue.next
                    index+=1
                newNode.next=tempvalue.next
                newNode.prev=tempvalue
                newNode.next.prev=newNode
                tempvalue.next=newNode
    def traversal(self):
        if self.head is None:
            print('there is not any element in the linked list')
        else:
            tempnode=self.head
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.next
    def reversetraversal(self):
        if self.head is None:
            print('there is not any element ')
        else:
            tempnode=self.tail
            while tempnode:
                print(tempnode.value)
                tempnode=tempnode.prev
    def search(self,nodevalue):
        if self.head is None:
            print('no element in the list')
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==nodevalue:
                    return tempnode.value
                tempnode=tempnode.next
            print('not found')
    def delete(self,location):
        if self.head is None:
            print('the list is empty')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=None
            elif location==-1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=None
            else:
                index=0
                tempnode=self.head
                while index < location-1:
                    tempnode=tempnode.next
                    index+=1
                tempnode.next=tempnode.next.next
                tempnode.next.prev=tempnode
            print('the node has been deleted')

    def deleteentire(self):
        if self.head is None:
            print('the linked list is empty')
        else:
            tempnode=self.head
            while tempnode:
                tempnode.prev=None
                tempnode=tempnode.next
            self.head=None
            self.tail=None
            print('successful deletion of entire doubly linked list')

doll=DoublyLinkedList()
doll.creation(45)
print([node.value for node in doll])
#tc=o(1)
#sc=o(1)
doll.insertion(34,0)
doll.insertion(56,1)
doll.insertion(23,-1)
print([node.value for node in doll])
doll.traversal()
print()
doll.reversetraversal()
print()
a=doll.search(29)
print(a)
print([node.value for node in doll])
doll.delete(2)
print([node.value for node in doll])
doll.deleteentire()
print([node.value for node in doll])