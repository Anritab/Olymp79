A = input().split()
B = []
for i in range(len(A)):
    if B.count(A[i])==0:
        B.append(A[i])
print(len(B))
