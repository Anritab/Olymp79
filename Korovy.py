n=int(input())
m=n%10
k=n%100
n = str(n)
if k>10 and k<20:
    print(n+' korov')
elif m==1:
    print(n+' korova')
elif m==2:
    print (n+' korovy')
elif m==3:
    print (n+' korovy')
elif m==4:
    print (n+' korovy')
else:
    print (n+' korov')
