d={}
count=0
str1=input("enter any string :")
str2='aeiouAEIOU'

for i in str1:
    if i in str2:
       if i in d:
           d[i]=d[i]+1
       else:
              d[i]=1
    
print(d)