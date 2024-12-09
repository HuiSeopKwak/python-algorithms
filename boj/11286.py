# 튜플을 이용하여 구현하면 첫째 값만으로 heap에 작은 순서대로 들어가기 때문에
# ex) (1, 1), (1, -1), (-2, 2) -> (1, -1), (1, 1), (-2, 2) 순으로 a비교 후 b비교로 정렬한다 ( 파이썬은 기본이 최소힙 )
#  튜플로 만들어 heap에 넣어준 후 heap에서 뽑아낼때 [1]의 값을 꺼낸다면
# 마이너스 값 또한 -를 붙여서 원래값을 찾아 낼 수 있다.
import sys
import heapq
input = sys.stdin.readline
max_heap = []
min_heap = []
result = []
# 나는 max_heap 에는 음수를 넣고 (abs로 넣어 절대값이 작은 순서대로)
# min_heap 에는 양수를 넣고 (절대값이 작은 순)
# 서로 값을 비교 후 더 작은 값이 있으면 그걸 뽑고, 둘이 같이 작은 값이라면 음수힙(max_heap)에서 값을 빼는 방법으로 구현할 예정
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