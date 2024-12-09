n = int(input())
dp = [0]*(n+3)
dp[1], dp[2], dp[3] = 1, 1, 2

for i in range(4, n+1):
    dp[i] = dp[i-2]*2 + dp[i-3]
    #dp[i-1] + dp[i-2] 랑 같다?!

print(dp[n])