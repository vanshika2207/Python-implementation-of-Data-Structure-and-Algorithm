class TrieNode:
    def __init__(self):
        self.children={}
        self.endofstring=False

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        current=self.root
        for i in word:
            ch=i
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.endofstring=True
        print('successfull')
    def searchstring(self,word):
        currentnode=self.root
        for i in word:
            node=currentnode.children.get(i)
            if node==None:
                return False
            currentnode=node
        if currentnode.endofstring==True:
            return True
        else:
            return False


newtrie=Trie()
newtrie.insert('app')
newtrie.insert('api')
print(newtrie.searchstring('appo'))