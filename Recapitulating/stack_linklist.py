class Node:
    def __init__(self,item):
        self.info=item
        self.next=None

class stack_linklist:
    def __init__(self):
        self.top=None
        self.start=None
        self.tail=None

    def push(self,item):
        nd=Node(item)

        if self.start==None and self.top==None:
            self.start=nd
            self.top=nd
            return
   
    
        self.top.next=nd
        self.top=nd


    def pop(self):
        if self.top==None:
            print("empty")

        item=self.top.info
        self.top=self.top.next




        