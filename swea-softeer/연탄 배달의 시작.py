n = int(input())
li = list(map(int, input().split()))
result = []
cnt = 0

for i in range(len(li)):
    for j in range(i+1, len(li)):
        result.append(li[j]-li[i])

minimum = min(result)

cnt = result.count(minimum)

print(cnt)