class stack:
    
    def __init__(self):
        self.top=-1
        self.stk=[0]*8

    def push(self,element):
        if self.top==7:
            print("stack is full")
        else:
            self.top+=1
            self.stk[self.top]=element
    
    def pop(self,element):
        if self.top==-1:
            print("stack is empty")
        else:
            element=self.stk[self.top]
            self.top-=1

    def display(self):
        if self.top==-1:
            print("stack is empty")
        else:
            for i in range(self.top,-1,-1):
                print(self.stk[i],end=" ")
        

obj=stack()

obj.push(10)
obj.pop(10)
obj.push(20)
obj.push(30)
obj.push(40)
obj.display()


