A = input().split()
k=10000000000000
for i in range(len(A)):
   A[i] = int(A[i])
   if A[i]>0:
       if A[i]<k:
          k=A[i]
print(k)
