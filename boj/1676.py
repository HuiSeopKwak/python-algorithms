N = int(input())
an = 1
for i in range(1, N+1):
    an *= i  

cnt = 0
check = True
num = str(an)
while check:
    for i in range(len(num)-1,-1,-1):
        if num[i] == '0':
            cnt += 1
        else:
            check = False
            break

print(cnt)
# 5의 배수 만큼 0의 갯수가 결정된다
# N이 500까지기 때문에 5, 25(5^2), 125(5^3)에 대해서만 나누어주면 된다
print(N//5 + N//25 + N//125)