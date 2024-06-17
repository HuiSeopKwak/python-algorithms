t = int(input())
nums = []
for i in range(t):
    num = int(input())
    nums.append(num)

dp = [[0, 0] for _ in range(50)]
dp[0][0], dp[0][1] = 1, 0
dp[1][0], dp[1][1] = 0, 1

for i in range(2, max(nums)+1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for i in nums:
    print(dp[i][0], dp[i][1])