k=int(input())
def IsPrime(n):
   d = 2
   while d * d <= n and n % d != 0:
       d += 1
   return d * d > n 

def NextPrime(n):
   while not IsPrime(n):
       n += 1
       if k==n:
           print(d)
           break        
   return n
    
