import sys
n, m = map(int, sys.stdin.readline().split())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
an = []

for i in range(n):
    for j in range(n):
        dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] - dp[i][j] + num[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    an.append(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])
    

print(*an, sep='\n')


## ======================================
## 완전탐색
"""
for i in range(m):
    sum = 0
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    for x in range(x1-1, x2):
        for y in range(y1-1, y2):
            sum += num[x][y]
    an.append(sum)

print(*an, sep='\n')
"""