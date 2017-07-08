input = open('input.txt', 'r')
S=input
input.close()
last_number = 0
for char in S:
    if '0' <= char <= '9':
        last_number = 10 * last_number + int(char)
    else:
        ans += last_number
        last_number = 0
output=open('output.txt','w')
output.write(last_number)
output.close()
