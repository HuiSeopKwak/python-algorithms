# 길 탐색은 bfs가 낫다
from collections import deque

Y, X = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(Y)]
print(graph)