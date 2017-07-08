
def summa_tsifr(i):
    s=0
    while(i>0):
        s+=i%10
        i=i//10
    return s
a = int(input())
b = int(input())
c = int(input())
for n in range(a, b+1):
    sum=summa_tsifr(n)
    if c==sum:
        print(n)


