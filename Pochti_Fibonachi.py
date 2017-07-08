F1=1
F2=1
F3=1
F4=0
n=int(input())
if n==0 or n==1 or n==2:
    print(1)
    
else:
    for i in range(3, n+1):
        F4=F1+F3
        F1=F2
        F2=F3
        F3=F4
    print(F3)
    
    
