F = int(input())
count = 1
phi1 = 1
phi2 = 1
phi3 = 0
for i in range (3, 20000000000):
    phi3=phi1+phi2
    print(phi3)
    if phi3==F:
        print(i)
        break
    elif phi3>F:
        print(-1)
        break
    else:
        phi1=phi2
        phi2=phi3
