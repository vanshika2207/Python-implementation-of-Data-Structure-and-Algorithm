#CREATION
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None
class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
            if node==self.tail.next:
                break

    def create(self,nodevalue):
        newnode=Node(nodevalue)
        self.head=newnode
        self.tail=newnode
        newnode.prev=newnode
        newnode.next=newnode
        return 'cdll is created succesfully'
    def insertion(self,nodevalue,location):
        newnode=Node(nodevalue)
        if self.head is None:
            return 'the cdll does not exist'
        else:

            if location==0:
                newnode.prev=self.tail
                newnode.next=self.head
                self.head.prev=newnode
                self.head=newnode
                self.tail.next=newnode
            elif location==-1:
                newnode.next=self.head
                newnode.prev=self.tail
                self.head.prev=newnode
                self.tail.next=newnode
                self.tail=newnode
            else:
                index=0
                tempnode=self.head
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1

                newnode.next=tempnode.next
                newnode.prev=tempnode
                newnode.next.prev=newnode
                tempnode.next=newnode

    def traversal(self):
        if self.head is None:
            print('empty linked list')
        else:
            tempnode=self.head
            while tempnode is not None:
                print(tempnode.value)

                if tempnode==self.tail:
                    break

                tempnode = tempnode.next


    def reversaltraversal(self):
        if self.head is None:
            print('empty linked list')
        else:
            tempnode=self.tail
            while tempnode :
                print(tempnode.value)
                if tempnode==self.head:
                    break
                tempnode=tempnode.prev
    def search(self,element):
        if self.head is None:
            print('empty linked list')
        else:
            tempnode=self.head
            while tempnode :
                if tempnode.value==element:
                    print(tempnode.value,'found')
                    break
                if tempnode==self.tail: #to prevent infinite loop
                    print('the value does not exist')
                    break
                tempnode=tempnode.next

    def delete(self,location):
        if self.head is None:
            return'the linked list is empty'

        else:
            if location==0:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
                    self.tail.next=self.head
            elif location==-1:
                if self.head==self.tail:
                    self.head.prev=None
                    self.head.next=None
                    self.head=None
                    self.tail=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head
                    self.head.prev=self.tail

            else:
                index=0
                tempnode=self.head
                while index< location-1:
                    tempnode=tempnode.next
                    index+=1
                tempnode.next=tempnode.next.next
                tempnode.next.prev=tempnode
    def entiredeletion(self):
        if self.head is None:
            return 'already empty'
        else:
            self.tail.next=None
            tempnode=self.head
            while tempnode:
                tempnode.prev=None
                tempnode=tempnode.next
            self.head=None
            self.tail=None





cdl=CircularDoublyLinkedList()
cdl.create(23)
cdl.insertion(34,0)
cdl.insertion(36,-1)
cdl.insertion(22,1)
cdl.insertion(56,2)
print([node.value for node in cdl])
cdl.traversal()
print()
cdl.reversaltraversal()
cdl.search(2)

print([node.value for node in cdl])
cdl.delete(2)
print([node.value for node in cdl])