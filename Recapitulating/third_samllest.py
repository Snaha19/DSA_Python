def third_smallest(l1):
    s1=s2=s3=float('inf')
    for i in l1:
        if i<s1:
            s3=s2
            s2=s1
            s1=i
        elif i<s2 and i!=s1:
            s3=s2
            s2=i
        elif i<s3 and i!=s2 and i!=s1:
            s3=i
    return s3
n=int(input("enter the number of elements :"))
l1=[]   
for i in range(n):
    l1.append(int(input("enter the element :")))
print("the third smallest element is :",third_smallest(l1))