case = int(input())
an = []
def findvalue(a1, b1):
    while b1>0:
        a1, b1 = b1, a1 % b1
    return a1

for _ in range(case):
    li = list(map(int, input().split()))
    sum = 0
    for i in range(1,len(li)-1):
        for j in range(i+1, len(li)):
            a, b = li[i], li[j]
            if a > b:
                sum += findvalue(a,b)
            elif a < b:
                sum += findvalue(b,a)
            else:
                sum += a
    an.append(sum)

for i in an:
    print(i)