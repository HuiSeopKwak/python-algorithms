n = int(input())

dp = [0]*(n+1)

if n > 1:
    dp[1], dp[2] = 3, 7
    for i in range(3, n+1):
        dp[i] = (dp[i-1]*2 + dp[i-2]) % 9901
elif n == 1:
    dp[1] = 3
    pass

print(dp[n] % 9901)