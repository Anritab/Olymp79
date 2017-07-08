n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))
m=A[0]
for i in range(n):
    if A[i]>m:
        m=A[i]
print(m)
