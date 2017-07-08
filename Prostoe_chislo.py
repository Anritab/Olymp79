k=int(input())
x=1
def IsPrime(n):
   d = 2
   while d * d <= n and n % d != 0:
       d += 1
   return d * d > n 

def NextPrime(n):
   while not IsPrime(n):
       n += 1
   return n 
for i in range(k):
    x=NextPrime(x+1)
print(x)

    
