n=int(input())
k=1
for i in range(1, n//2+1):
    if n%i==0:
        k+=1
print(k)
