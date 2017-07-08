s1=int(input())
s2=int(input())
s3=int(input())
s4=int(input())
ss=0
if s1>=s2 and s3>=s4:
    for s in range(s2, s1+1):
        print(s)
        for sss in range(s4, s3+1):
            if s==sss:
                ss+=1
if s1<s2 and s3>s4:
    for s in range(s1, s2+1):
        for sss in range(s4, s3+1):
            if s==sss:
                ss+=1
if s1>s2 and s3<s4:
    for s in range(s2, s1+1):
        for sss in range(s3, s4+1):
            if s==sss:
                ss+=1
if s1<=s2 and s3<=s4:
    for s in range(s1, s2+1):
        for sss in range(s3, s4+1):
            if s==sss:
                ss+=1
print(ss)
    
