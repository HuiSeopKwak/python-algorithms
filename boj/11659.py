import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # n 숫자 수 m 합 구해야 하는 수
nums = list(map(int, input().split()))
nums.insert(0, 0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    dp[i] = dp[i-1] + nums[i]

for _ in range(m):
    a, b = map(int, input().split()) # a, b 구간
    print(dp[b] - dp[a-1])