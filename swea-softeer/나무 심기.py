n = int(input())
li = list(map(int, input().split()))
result = []

for i in range(len(li)):
    for j in range(i+1, len(li)):
        result.append(li[i]*li[j])

print(max(result))