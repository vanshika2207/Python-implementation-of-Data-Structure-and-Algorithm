class binarytree:
    def __init__(self,size):
        self.customlist=[None]*size
        self.lastusedindex=0
        self.maxsize=size
    def insertnode(self,node):
        if self.lastusedindex+1==self.maxsize:
            return 'already full'
        self.customlist[self.lastusedindex+1]=node
        self.lastusedindex+=1
        return
    def search(self,nodevalue):
        for i in range(len(self.customlist)):
            if self.customlist[i]==nodevalue:
                return 'success'
        return 'not found'
    def preorder(self,index):
        if index>self.lastusedindex:
            return
        print(self.customlist[index])
        self.preorder(index*2)
        self.preorder(index*2+1)
    def postorder(self,index):
        if index>self.lastusedindex:
            return
        self.postorder(index * 2)
        self.postorder(index * 2 + 1)
        print(self.customlist[index])
    def inorder(self,index):
        if index>self.lastusedindex:
            return
        self.inorder(index * 2)
        print(self.customlist[index])
        self.inorder(index * 2 + 1)
    def levelorder(self,index):
        for i in range(index,self.lastusedindex+1):
            print(self.customlist[i])
    def deletenode(self,value):
        if self.lastusedindex==0:
            return 'empty binary tree '
        for i in range(1,self.lastusedindex+1):
            if self.customlist[i]==value:
                self.customlist[i]==self.customlist[self.lastusedindex]
                self.customlist[self.lastusedindex]==None
                self.lastusedindex-=1
                return 'successfully deleted'
    def deleteentire(self):
        self.customlist=None
        print('successful')








newbt=binarytree(8)
newbt.insertnode('n1')
newbt.insertnode('n2')
newbt.insertnode('n3')
newbt.insertnode('n4')
newbt.insertnode('n5')
newbt.insertnode('n6')
newbt.insertnode('n7')
newbt.insertnode('n8')
print(newbt.customlist)
print(newbt.search('n4'))
print(newbt.search('n8'))
newbt.preorder(1)
print()
newbt.postorder(1)
print()
newbt.inorder(1)
print()
newbt.levelorder(1)
newbt.deletenode('n7')
print()
newbt.levelorder(1)
newbt.deletenode('n1')
print(newbt.customlist)
print(newbt.deleteentire())
print(newbt.customlist)
