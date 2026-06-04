def heapify(A,i,n):
    l=2*i+1
    r=2*i+2
    lar=i

    if r<n and A[r]>A[lar]:
        lar=r
    if l<n and A[l]>A[lar]:
        lar=l

    if lar==i:
        return
    if lar!=i:
        A[i],A[lar]=A[lar],A[i]
        heapify(A,lar,n)



def max_heap(A,n):
    for i in range(n//2+1,-1, -1):
        heapify(A,i,n)

def heap_sort(A,size):
    n=size
    while n>=1:
        A[0],A[n-1]=A[n-1],A[0]
        n=n-1
        heapify(A,0,n)




A=[40,30,65,60,35,49,50,55,25,28]
size=len(A)
print(A)
print("max heap")
max_heap(A,size)
print(A)
heap_sort(A,size) 
print("After soting :")
print(A)
