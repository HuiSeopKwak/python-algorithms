import sys
input = sys.stdin.readline


n = int(input())
price = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = price[0][0], price[0][1], price[0][2]

for idx in range(n-1):
    dp[idx+1][0] = min(dp[idx][1], dp[idx][2]) + price[idx+1][0]
    dp[idx+1][1] = min(dp[idx][0], dp[idx][2]) + price[idx+1][1]
    dp[idx+1][2] = min(dp[idx][0], dp[idx][1]) + price[idx+1][2]

print(min(dp[n-1]))