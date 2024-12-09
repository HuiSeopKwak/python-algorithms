import sys

n = int(sys.stdin.readline().rstrip())
li = list(list(map(int, sys.stdin.readline().split())) for i in range(n))
li.sort()

highest = 0
highest_index = 0

result = 0
height = li[0][1]
# 왼쪽에서 최고점까지
for i in range(n):
    if li[i][1] > highest:
        highest = li[i][1]
        highest_index = i

for i in range(highest_index):
    if li[i+1][1] > height: # 끊기고 더 올라가야함
        result += height * (li[i+1][0] - li[i][0])
        height = li[i+1][1]
    else:                   # 안 끊기고 오른쪽으로 천장쌓아감
        result += height * (li[i+1][0] - li[i][0])

#반대에서 최고점으로
height = li[-1][1]

for i in range(len(li)-1, highest_index, -1):
    if li[i-1][1] > height: 
        result += height * abs(li[i-1][0] - li[i][0])
        height = li[i-1][1]
    else:                  
        result += height * abs(li[i-1][0] - li[i][0])

#가장 높은 기둥 마지막에 더해줌
result += li[highest_index][1]

print(result)