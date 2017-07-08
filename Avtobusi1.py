N=int(input())
A=int(input())
B=int(input())
PA=A/50
PB=B/4
Bus = 0;
Taxi = 0;

L = N%100        


P1 = 2*A

P2Taxi=(L-50)//4
if (L-50)%4:
        P2Taxi+=1

if (L-50)<0:
    P2Taxi=0

P2= A + B*P2Taxi

P3Taxi=L//4
if L%4:
    P3Taxi+=1

P3 = B*P3Taxi

if P1 < P2:
    if P1<P3:
        Bus+=2
    else:
        Taxi+=P3Taxi
else:
    if P2 < P3:
        Bus+=1
        Taxi+=P2Taxi
    else:
        Taxi+=P3Taxi

if PA<PB:
    Bus = Bus + (N-N%100)//50
else:
    Taxi = Taxi + (N-N%100)//4
print(Bus, Taxi, sep=' ')
