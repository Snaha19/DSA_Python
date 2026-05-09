def quicksort(A,l,r):
    if (l<r):
        p=quick(A,l,r)
        quicksort(A,l,p-1)
        quicksort(A,p+1,r)

def quick(A,l,r):    
    p=l
    left=l+1
    right=r
   

    while(True):
       
        while left<=right and A[p] <= A[right]   :
            right=right-1

        if A[p] > A[right] :
            A[p],A[right]=A[right],A[p]
            p=right
            right=right-1
            

        if right <left :
            return p    
            


        while left <= right  and A[p] >= A[left]  :
            left=left+1

        if A[p] < A[left] :
            A[p],A[left]=A[left],A[p]
            p=left
            left=left+1
        
    
        if right < left :
            return p
        
    
     
            

A=[0,17,-3,90,-14,0,1,100]
r=len(A)-1
l=0

quicksort(A,l,r)
print(A)