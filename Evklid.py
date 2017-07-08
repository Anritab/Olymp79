n=int(input())
k=int(input())
while n!=k:
    if n>k:
        n-=k
    else:
        k-=n
print(n)
