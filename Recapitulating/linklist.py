class node:

    def __init__(self,item):
        self.info=item
        self.next=None

class single_linklist:
    def __init__(self):
        self.start=None


    def insert_at_last(self,item):
        nd=node(item)
        if self.start==None:
            self.start=nd
            return
        temp=self.start
        while temp.next!=None:
            temp=temp.next
        temp.next=nd

    def insert_at_beginning(self,item):
        nd=node(item)
        nd.next=self.start
        self.start=nd

    def display(self):
        temp=self.start
        while temp!=None:
            print(temp.info)
            temp=temp.next


    def insert_at_position(self,item,position):
        if position==1:
            self.insert_at_beginning(item)
        else:
            nd=node(item)
            i=1
            temp=self.start
            while temp.next != None and i<position :
                #prev=temp
                temp=temp.next
                i=i+1

        if temp.next==None:
            temp.next=nd
            return
        
        nd.next=temp.next
        temp.next=nd

    
    def insert_before_specific_item(self,item,specific_item):
        nd=node(item)
        temp=self.start
        prev=None

        while  temp.next!=None and specific_item!=temp.info:
            #  prev=temp
             temp=temp.next
        
        # if prev==None:
        #     self.insert_at_beginning(item)
        #     return
        nd.next=temp.next
        temp.next=nd

    def insert_after_specific_item(self,item,specific_item):
        nd=node(item)
        temp=self.start

        while  temp.next!=None and specific_item!=temp.info:
             temp=temp.next
        
        if temp.next==None and specific_item!=temp.info:
            print("item not found")
            return
        nd.next=temp.next
        temp.next=nd 

    def delete_start_node(self):
        temp=self.start

        self.start=temp.next
        del temp

    def delete_last_node(self):
        temp=self.start
      
        while temp.next!=None:
            prev=temp
            temp=temp.next

        prev.next=None
        del temp

    def delete_specific_position(self,position):
        temp=self.start
        i=1
        while temp.next!=None and i<position :
            prev=temp
            temp=temp.next 
            i+=1

        prev.next=temp.next
        del temp


    



sl= single_linklist()
sl.insert_at_beginning(10)
sl.insert_at_beginning(20)
sl.insert_at_beginning(30)
sl.insert_at_last(500) 
sl.display()
# print("after calling insert_at specific position function")
# sl.insert_at_position(900,3)
# sl.display()
print("after inserting at specific item ")
sl.insert_after_specific_item(900,30)
sl.display()
# print("ater deleting a sprcific position")
# sl.delete_specific_position(3)
# sl.display()
