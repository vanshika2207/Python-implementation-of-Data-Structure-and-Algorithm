import QueueLinkedList as queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
newbt=TreeNode("N1")
leftchild=TreeNode("N2")
rightchild=TreeNode("N3")
newbt.leftchild=leftchild
newbt.rightchild=rightchild
def preorder(rootnode):
    if not rootnode:
        return
    print(rootnode.data)
    preorder(rootnode.leftchild)
    preorder(rootnode.rightchild)
preorder(newbt)
def inorder(rootnode):
    if not rootnode:
        return
    inorder(rootnode.leftchild)
    print(rootnode.data)
    inorder(rootnode.rightchild)
print()
inorder(newbt)
print()
def postorder(rootnode):
    if not rootnode:
        return
    postorder(rootnode.leftchild)
    postorder(rootnode.rightchild)
    print(rootnode.data)
postorder(newbt)
print()

def levelorder(rootnode):
    if not rootnode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root=customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftchild is not  None):
                customqueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customqueue.enqueue(root.value.rightchild)
levelorder(newbt)
def search(rootnode,nodeValue):
    if not rootnode:
        print('binary root not exist')
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root=customqueue.dequeue()
            if root.value.data==nodeValue:
                print('successful')
            if (root.value.leftchild is not None):
                customqueue.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                customqueue.enqueue(root.value.rightchild)
        return ('not found')
search(newbt,'N2')
def insertnode(rootnode,newnode):
    if not rootnode:
        rootnode=newnode
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root=customqueue.dequeue()
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild=newnode
                return'successfull'
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newnode
                return 'successfull'
newnode=TreeNode('N4')
insertnode(newbt,newnode)
levelorder(newbt)
print()
def getdeepest(rootnode):
    if not rootnode:
        return
    else:
        customqueue=queue.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isEmpty():
            root=customqueue.dequeue()
            if root.value.leftchild is not None:
                customqueue.enqueue((root.value.leftchild))
            if root.value.rightchild is not None:
                customqueue.enqueue((root.value.rightchild))
        deep=root.value
        return deep
a=getdeepest(newbt)
print(a)

print()
def deletedeepest(rootnode,deepest):
    if rootnode is None:
        return
    else:
        cq=queue.Queue()
        cq.enqueue(rootnode)
        while not(cq.isEmpty()):
            root=cq.dequeue()
            if root.value.data is deepest:
                root.value.data=None
                return
            if root.value.leftchild:
                if root.value.leftchild is deepest:
                    root.value.leftchild =None
                    return
                else:
                    cq.enqueue(root.value.leftchild)
            if root.value.rightchild:
                if root.value.rightchild is deepest:
                    root.value.rightchild =None
                    return
                else:
                    cq.enqueue(root.value.rightchild)
def deletenode(rootnode,node):
    if not rootnode:
        return
    else:
        cq=queue.Queue()
        cq.enqueue(rootnode)
        while not(cq.isEmpty()):
            root=cq.dequeue()
            if root.value.data==node:
                dnode=getdeepest(rootnode)
                root.value.data=dnode.data
                deletedeepest(rootnode,dnode)
                return 'node successfully deleted'
            if (root.value.leftchild is not  None):
                cq.enqueue(root.value.leftchild)
            if (root.value.rightchild is not None):
                cq.enqueue(root.value.rightchild)
        return 'Failed'
print(deletenode(newbt,'N3'))
levelorder(newbt)
print()
def deletebt(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted"
print(deletebt(newbt))
inorder(newbt)
