import sys
sys.setrecursionlimit(100_000_000)

def recur(x, y):
    if dp[y][x] != 0:
        return dp[y][x]

    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ex = dx + x
        ey = dy + y
        if 0 <= ex < n and 0 <= ey < n:
            if forest[y][x] < forest[ey][ex]:
                dp[y][x] = max(dp[y][x], recur(ex, ey) + 1)
    
    return dp[y][x]

n = int(input())

forest = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        recur(i, j)

print(max(map(max, dp)) + 1)