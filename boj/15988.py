n = int(input())
li = [int(input()) for _ in range(n)]
biggestnum = max(li) + 1
dp = [0]*max(biggestnum,3)
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, biggestnum):
    dp[i] = dp[i-1]%1000000009 + dp[i-2]%1000000009 + dp[i-3]%1000000009

for i in li:
    print(dp[i]%1000000009)