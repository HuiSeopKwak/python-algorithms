import sys
import heapq
input = sys.stdin.readline
heap = []
result = []

n = int(input())
for _ in range(n):
    a = int(input())
    if a == 0:
        if len(heap) != 0:
            result.append(heapq.heappop(heap))
        else:
            result.append(0)
    else:
        heapq.heappush(heap, a)

for i in result:
    print(i)