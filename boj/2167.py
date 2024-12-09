a, b = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(a)]
n = int(input())
li1 = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(b+1)] for _ in range(n+1)]