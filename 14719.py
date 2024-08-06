h, w = map(int, input().split())

li = list(map(int, input().split()))
max_left, max_right = 0, 0
result = 0

for i in range(1, w-1):
    max_left = max(li[:i])
    max_right = max(li[i+1:])
    height = min(max_left, max_right)
    if  height > li[i]:
        result += height - li[i]
    else:
        continue

print(result)