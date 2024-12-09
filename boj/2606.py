from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
q = deque()
q.append(1)

while len(q) > 0:
    node = q.popleft()
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        q.append(nxt)

print(visited)

# dfs 풀이
"""
def recur(node):
    visited[node] = 1
    for nxt in graph[node]:
        if visited[nxt] == 1:
            continue
        recur(nxt)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
    
recur(1)

print(sum(visited)-1)
"""