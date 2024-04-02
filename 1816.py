n = int(input())
s = list(int(input()) for _ in range(n))

for num in s:
    check = True
    for i in range(2, 1000000):
        if num % i == 0:
            print('NO')
            check = False
            break
    if check == True:
        print('YES')