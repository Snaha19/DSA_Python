class Node:
    def __init__(self,item):
        self.info=item
        self.next=None

class circular_linklist:
    def __init__(self):
        self.start=None

    def insert_at_last(self,item):
        nd=Node(item)

        if self.start==None:
            self.start=nd
            nd.next=self.start
            return
        
        temp=self.start
        
        while(temp.next!=self.start):
            temp=temp.next
        temp.next=nd
        nd.next=self.start
    

    def display(self):
        temp=self.start

        while(temp.next !=self.start):
            print(temp.info,sep=" ",end="  ->  ")
            temp=temp.next
        print(temp.info,end="  ->  ")
        print("start")
       
        # while True:
        #     print(temp.info, end=" -> ")
        #     temp = temp.next

        #     if temp == self.start:
        #       break
            

    def insert_at_beggining(self,item):
        nd=Node(item)

        if self.start==None:
            self.start=nd
            nd.next=self.start
            return
        
        temp=self.start
        while(temp.next!=self.start):
            temp=temp.next
       
        nd.next=self.start
        self.start=nd
        temp.next=nd



    def insert_at_specific_position(self,item,position):
        nd=Node(item)

        if position==0:
            self.insert_at_beggining(item)
            return
        
        temp=self.start
        i=0
        # prev=temp
        # while temp.next!=self.start and  i<position:
        #     prev=temp
        #     temp=temp.next
        #     i+=1
            # nd.next=temp
            # prev.next=nd
        
        while temp.next!=self.start and  i<position-1:
            temp=temp.next
            i=i+1
        nd.next=temp.next
        temp.next=nd


    def insert_after_specific_item(self,item,find):
        nd=Node(item)
        temp=self.start
        while temp.next!=self.start and temp.info!=find:
            temp=temp.next
        
       
        nd.next=temp.next
        temp.next=nd


    def delete_last(self):
        temp=self.start
        p=self.start
        if self.start.next == self.start:
            self.start = None
            return

        while temp.next!=self.start:
            p=temp
            temp=temp.next

        p.next=self.start
        del temp

    def delete_begging(self):
       temp=self.start
       if self.start==None:
           return
       
       if self.start.next == self.start:
        self.start = None
        return
              
       while temp.next!=self.start:
          temp=temp.next
         

       temp.next=self.start.next
       self.start=self.start.next
       
       
        



cl=circular_linklist()
# cl.insert_at_last(10)
# cl.insert_at_last(90)
# cl.insert_at_last(100)
cl.insert_at_beggining(40)
cl.insert_at_beggining(30)
cl.insert_at_beggining(20)
cl.insert_at_beggining(10)
cl.display()
#cl.insert_at_specific_position(77,2)
cl.insert_after_specific_item(55,40)
cl.insert_after_specific_item(66,55)
cl.delete_last()
cl.delete_begging()
cl.delete_begging()
cl.display()