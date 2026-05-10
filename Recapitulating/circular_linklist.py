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

    
        if temp == None:
          print("Nothing to show")
          return
        
        else:
            
          while True:
            print(temp.info, end=" -> ")
            temp = temp.next

            if temp == self.start:
                break
        print("start")
        
            
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

       
    def delete_specific_position(self,position):
        if position==0:
            self.delete_begging()
            return
        
        temp=self.start
        i=0
       
        while temp.next!=self.start and i<position:
            p=temp
            temp=temp.next
            i+=1


        p.next=temp.next
        del temp

    def delete_specific_item(self,item):
            temp=self.start

            if self.start.info==item:
                self.delete_begging()
                return
            if self.start.info==item and self.start.next==self.start:
                self.delete_begging()
            p=temp
            while temp.next!=self.start and temp.info!=item:
                p=temp
                temp=temp.next
           
            
           
            if temp.info==item:
                 p.next=temp.next

            else:
                print("item not found")
                return

        
       
        


        



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
# cl.insert_after_specific_item(55,40)
# cl.insert_after_specific_item(66,55)
# cl.delete_last()
# cl.delete_begging()
# cl.delete_begging()
cl.delete_specific_position(3)
cl.delete_specific_position(2)
cl.delete_specific_position(1)
cl.delete_specific_position(0)
# cl.delete_specific_item(40)
# cl.delete_specific_item(10)
# cl.delete_specific_item(30)
# cl.delete_specific_item(20)

cl.display()