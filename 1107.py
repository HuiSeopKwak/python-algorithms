n = int(input())
num = int(input())
if num > 0:
    broken = list(map(int, input().split()))
min_count = abs(n-100)

for i in range(1000001):
    if num == 0:
        break
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in broken:
            break
        elif j == len(i)-1:
            min_count = min(min_count, abs(int(i)-n)+len(i))
            
if num != 0:
    print(min_count)
else:
    print(len(str(n)))

    #틀렸음