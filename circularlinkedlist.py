class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class CircularSinglyLinkedList:
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
    def create(self,nodeValue):
        node=Node(nodeValue)
        node.next=node
        self.head=node
        self.tail=node
        print( 'csll is created')
    def insertion(self,newvalue,location):
        newnode=Node(newvalue)
        if self.head is None:
            return'the head refernce is None'
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
                self.tail.next=newnode
            elif location==-1:
                newnode.next=self.tail.next
                self.tail.next=newnode
                self.tail=newnode
            else:
                tempnode=self.head
                index=0
                while index<=location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=newnode
                newnode.next=nextnode

            return 'the node is succesfully completed'
    def traversal(self):
        if self.head is None:
            print('sorry')
        else:
            tempnode=self.head
            while tempnode :
                print(tempnode.value)
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    break

    def search(self,node):
        if self.head is None:
            print('sorry')
        else:
            tempnode=self.head
            while tempnode:
                if tempnode.value==node:
                    return tempnode.value
                tempnode=tempnode.next
                if tempnode==self.tail.next:
                    return"sorry node does not exist"
    def delete(self,location):
        if self.head is None:
            print('sorry linked list does not exist')
        else:
            if location==0:
                if self.head==self.tail:
                    self.head.next=None
                    self.head=None
                    self.tail=None

                else:
                    self.head=self.head.next
                    self.tail.next=self.head
            elif location==-1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None

                else:
                    tempnode=self.head
                    while tempnode is not None:
                        if tempnode.next==self.tail:
                            break
                        tempnode=tempnode.next
                        tempnode.next=self.head
                        self.tail=self.head
            else:
                tempnode=self.head
                index=0
                while index<location-1:
                    tempnode=tempnode.next
                    index+=1
                nextnode=tempnode.next
                tempnode.next=nextnode.next
    def deletefull(self):
        if self.head is None:
            print('linked list does not exist')
        else:
            self.head=None
            self.tail.next=None
            self.tail=None










cssl=CircularSinglyLinkedList()
cssl.create(1)
cssl.insertion(9,0)
cssl.insertion(2,2)
cssl.insertion(4,-1)
print([node.value for node in cssl])
cssl.traversal()
cssl.search(8)
cssl.traversal()
print([node.value for node in cssl])
cssl.delete(-1)
cssl.deletefull()
print([node.value for node in cssl])