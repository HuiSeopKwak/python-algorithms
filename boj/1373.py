n = int(input(),8)
print(bin(n)[2:])



""" 시간 초과 코드
for i in range(len(n)):
    sum += int(n[i])*(2**(len(n)-i-1))
an = []

while sum>0:
    an.append(sum%8)
    sum = sum//8

for i in range(len(an)-1,-1,-1):
    print(an[i], end='')
"""