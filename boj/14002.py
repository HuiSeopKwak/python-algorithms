n = int(input())
li = list(map(int, input().split()))
dp = [1]*n
prev_index = [-1]*n
result = []

for i in range(1, n):
    for j in range(i):
        if li[j] < li[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j]+1
            prev_index[i] = j

maxindex = dp.index(max(dp))

while prev_index[maxindex] != -1:
    result.append(li[maxindex])
    maxindex = prev_index[maxindex]
result.append(li[maxindex])

print(max(dp))
for i in reversed(result):
    print(i, end=' ')