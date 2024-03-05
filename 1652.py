import sys
k, n = map(int, input().split())
length = []

for i in range(k):
    length.append(int(sys.stdin.readline()))

end = max(length)
start = 1

while start <= end:
    mid = (start + end) // 2
    lines = 0
    for i in length:
        lines += i // mid
    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1
print(end)