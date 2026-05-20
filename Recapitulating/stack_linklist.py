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
   
    
        # self.top.next=nd
        # self.top=nd
        nd.next=self.top
        self.top=nd

    def pop(self):
        if self.top==None:
            print("empty")

        item=self.top.info
        self.top=self.top.next
        del item
    
    def display(self):
        temp=self.top
        while(temp!=None):
            print(temp.info)
            temp=temp.next


s=stack_linklist()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
print("delete")
s.display()

        