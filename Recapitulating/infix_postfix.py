l=[5,'+','(',10,'-',2,')','*',3]
List_oprator=['+','*','/','-','^','$','**']
p=[0]*len(l)


def precedence(op):
            if op=='$' or op=='^' or op=='**':
                return 40         
            if op=='*' or op=='/' or op=='%':
                return 3

            if op=='+' or op=='-':
                return 2
            
def __init__(self):
            self.top=-1
            self.stk=[0]*len(l)
            
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

for i in l:
        if i in List_oprator:
                r=precedence(i)

        if i =='(':
                push(i)

        if i==')':
                pass
        
        else:
              p.append(i)  