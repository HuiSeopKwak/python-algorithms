n, k = map(int, input().split())
value = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
bagsvalue = [0]*k
bags.sort()

for i in range(n):
    if value[i][0] <= bags[-1]:
        for j in range(k):
            if bagsvalue[j] < value[i][1] and bags[j] >= value[i][0]:
                bagsvalue[j] = value[i][1]
                break

print(bagsvalue)
