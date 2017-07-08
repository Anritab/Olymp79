k=0
for i in range(100000, 1000000):
    if i%2!=0 and i%5!=0 and i%7!=0:
        k+=1
print(k)
