class Node:
    def __init__(self,item):
        self.info=item
        self.right=None
        self.left=None

class binary_search_tree:
    def __init__(self):
        self.root=None

    def insert(self,item):
        nd=Node(item)

        if self.root==None:
            self.root=nd
            return
        
        temp=self.root
        while temp!=None:
            if item<temp.info:
                parent=temp
                temp=temp.left
            else:
                parent=temp
                temp=temp.right
        if item<parent.info:
            parent.left=nd
        else:
            parent.right=nd

    def search(self,item):
        temp=self.root
        parent=temp

        if self.root==None:
            print("empty")
            return
        while temp!=None:
            if item==temp.info:
                print("item found")
                return parent.temp
            elif item<temp.info:
                parent=temp
                temp=temp.left
            else:
                parent=temp
                temp=temp.right
        if temp==None:
            print("not found")
            return parent,temp



    

def inorder(nd):

        if nd!=None:
            inorder(nd.left)
            print(nd.info)
            inorder(nd.right)


bst=binary_search_tree()
bst.insert(100)
bst.insert(50)
bst.insert(150)
bst.insert(30)
bst.insert(80)
bst.insert(60)
bst.insert(120)
bst.insert(180)
bst.insert(140)
        
inorder(bst.root)
