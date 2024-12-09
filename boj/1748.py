an = 0

num = int(input()) 
strnum = str(num)   #num의 문자형
size = len(strnum)  #num 문자형의 길이(개수 계산을 위해서)

for i in range(size, 0, -1):
    if i == size:
        an += size*(num-(10**(i-1)-1))
    else:
        an +=  i*(10**i - 10**(i-1))
print(an)