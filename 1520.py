import sys
input = sys.stdin.readline
sys.setrecursionlimit(100_000_000)

def recur(y, x):
    global count
    if y == m-1 and x == n-1:
        count += 1
    for dx, dy in [[1,0], [-1,0], [0,1], [0,-1]]:
        ey = y + dy
        ex = x + dx
        if 0 <= ex < n and 0 <= ey < m:
            if height[y][x] > height[ey][ex]:
                recur(ey, ex)


m, n = map(int, input().split())
height = [list(map(int, input().split())) for _ in range(m)]
count = 0

recur(0, 0)
print(count)