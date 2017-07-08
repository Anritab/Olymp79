N=int(input())
A = []
count=0
for i in range(N):
    A.append(int(input()))
    if A[i]>0:
        count+=1 
print(count)
