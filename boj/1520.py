import sys
input = sys.stdin.readline
sys.setrecursionlimit(100_000_000)

def recur(y, x):
    if x == n-1 and y == m-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    route = 0
    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
        ey = y + dy
        ex = x + dx
        if 0 <= ex < n and 0 <= ey < m:
            if height[y][x] > height[ey][ex]:
                route += recur(ey, ex)
                # dp[y][x] = max((dp[y][x]), recur(ey,ex) + 1)
    
    dp[y][x] = route
    return dp[y][x]


m, n = map(int, input().split())        # m은 y 범위, n은 x 범위
height = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1 for _ in range(n)] for _ in range(m)]

print(recur(0, 0))
