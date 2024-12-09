import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
result = []

for i in range(n):
    a = int(input())
    if a == 0: # 최대힙 빼기
        if len(heap) != 0:
            result.append(-heapq.heappop(heap))
        else:
            result.append('0')
    else:
        heapq.heappush(heap, -a)

for i in result:
    print(i)