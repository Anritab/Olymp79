N=int(input())
A=int(input())
B=int(input())
PA=A/50
PB=B/4

Bus = N//50
if Bus%50:
    Bus+=1
Taxi = N//4
if Taxi%4:
    Taxi+1

if Taxi*B<Bus*A:
    Bus = 0
else:
    Bus=N//50
    if N%50:
        L=N%50
        Taxi=L//4
        if L%4:
            Taxi+=1
        if B*Taxi>=A:
            Bus+=1
            Taxi=0
print(Bus, Taxi, sep=' ')
