# 이모스법 을 적용하여 풀어볼 것임
import sys
input = sys.stdin.readline
li = []
n, m = map(int, input().split())

for i in range(n):
    li.append(int(input()))

height = [0 for i in range(m)]
for i in range(n):
    if i % 2 == 0:
        height[0] += 1
        height[li[i]] -= 1
    else:
        height[m-li[i]] += 1
for i in range(1,len(height)):
    height[i] += height[i-1]

shortest = min(height)
count = height.count(shortest)

print(shortest, count)