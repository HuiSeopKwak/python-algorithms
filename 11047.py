n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
total = 0

for i in range(len(coin)-1, -1, -1):
    if coin[i] <= k:
        cnt = k // coin[i]
        total += cnt
        k -= coin[i]*cnt
    if k == 0:
        break

print(total)