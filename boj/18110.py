import sys

n = int(input())
sum = 0
def cal(num):
    if num - int(num) >= 0.5:
        num = int(num)+1
    return int(num)

li = []
for i in range(n):
    li.append(int(sys.stdin.readline().rstrip()))

outsider = cal(n * 0.15)

li.sort()

for i in range(outsider, n-outsider):
    sum += li[i]
if len(li[outsider:n-outsider]) != 0:
    result = sum / len(li[outsider:n-outsider])
else:
    result = 0

print(cal(result))