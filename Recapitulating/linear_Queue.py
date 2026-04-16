class Queue:
    
    def __init__(self):
        self.rear=-1
        self.front=-1
        self.que=[0]*8

    def insertion(self,element):
        if self.front==7 and self.rear==7:
            print(" queue is overflow")
        else:
            self.front=self.front+1
            self.que[self.front]=element
            if self.rear==-1:
                self.rear=0

    
    def deletion(self,element):
        if self.rear==-1 and self.front==-1:
            print("queue is underflow ")
        else:
            element=self.que[self.rear]
            if self.front==self.rear:
                self.front=-1 
                self.rear=-1
            else:
                self.rear+=1

    def display(self):
        if self.rear==-1:
            print("queue is empty")
        else:
            for i in range(self.front,0,-1):
                print(self.que[i],end=" ")
        
obj=Queue()
obj.deletion(10)
obj.insertion(12)
obj.insertion(7)
obj.deletion(12)
obj.display()