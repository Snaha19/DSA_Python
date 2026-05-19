class Node:
    def __init__(self,coef,expo):
        self.coef=coef
        self.expo=expo
        self.next=None

class poly:
    def __init__(self):
        self.start=None
    def insert(self,coef,exp):
        nd=Node(coef,exp)
        temp=self.start
        prev=temp
        if self.start==None or exp>self.start.expo: #insert at begining or in emty polynomial
            nd.next=self.start
            self.start=nd
            return
      
        while temp.next!=None and temp.expo>exp:    #loop for searching proper position of th new term
            prev=temp
            temp=temp.next

        if temp.expo<exp: # when new term would be inserted before temp
            nd.next=temp
            prev.next=nd
            return
        if temp.next==None:   # new term would be inserted at last
            #nd.next=temp.next
            temp.next=nd


    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.coef,end="")
            print("x^",end="")
            print(temp.expo,end="")
            if temp.next!=None:
              print(" + ",end="")
            temp=temp.next
        
p=poly()

p.insert(2,4)
p.insert(2,3)
p.insert(21,1)

p.insert(2,2)
p.insert(1,0)
p.display()