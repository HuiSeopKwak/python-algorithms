import sys
input = sys.stdin.readline

def recur(idx, weight):
    global an
    if weight > k:
        return -999999
    if idx == n:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]

    dp[idx][weight] = max(recur(idx+1, weight + product[idx][0]) + product[idx][1], recur(idx+1, weight))
    
    return dp[idx][weight]
    
n, k = map(int, input().split())
product = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(100_001)] for _ in range(n)]

an = recur(0, 0)

print(an)

#이해가 안돼