A=[]
for i in range(1, 101):
    A.append(i)
i=-1
while len(A)>1:
    i+=19
    while i>=len(A):
        i=i-len(A)
    print(A[i])
    A.pop(i)
    i-=1

print(A[0])
