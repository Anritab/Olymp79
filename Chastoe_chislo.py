A = input().split()
k=0
n=0
for i in range(len(A)):
    A[i]=int(A[i])
    if A.count(A[i])>k:
        k=A.count(A[i])
        n=A[i]
    elif A.count(A[i])==k:
        if A[i]>n:
            n=A[i]
print(n)
        
