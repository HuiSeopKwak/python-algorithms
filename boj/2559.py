n, k = map(int, input().split())
li = list(map(int, input().split()))
prefix = [0 for _ in range(n+1)]
an = []

for i in range(n):
    prefix[i+1] = prefix[i] + li[i]

for i in range(k, n+1):
    an.append(prefix[i] - prefix[i-k])

print(max(an))