N = int(input())
M = int(input())
result = ""
if N>2*M or M>2*N:
    result = 'NO SOLUTION'
elif M>N:
    while not M==N:
        result+="GBG"
        M-=2
        N-=1
    while not M==0:
        result+="GB"
        M-=1
elif M<N:
    while not M==N:
        result+="BGB"
        N-=2
        M-=1
    while not N==0:
        result+="BG"
        N-=1
elif M==N:
    result="BG"*N
print(result)
