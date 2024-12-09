# 간단한 369게임

n = int(input())

for i in range(1, n+1):
    count = 0
    for num in str(i):
        if num == '3':
            count += 1
        if num == '6':
            count += 1
        if num == '9':
            count += 1
    if count == 0:
        print(i, end =" ")
    else:
        for j in range(count):
            print('-', sep="",end="")
        print(" ", end="")