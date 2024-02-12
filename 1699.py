n = int(input())
dp = [x for x in range(n+1)]
for i in range(2, n+1):
    j = 1
    while j * j <= i:
        square = j*j
        if dp[i] > dp[i - square] + 1:
            dp[i] = dp[i - square] + 1
        j += 1

print(dp[n])