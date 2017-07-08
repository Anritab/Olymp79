flag=1
for i in range(100000000000000, 999999999999999):
    for k in range(2, i//2):
        if i%k==0:
            flag=0
            break
    print(i)
    if flag!=0:
        print(i)
        break
