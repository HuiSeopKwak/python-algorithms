# 2644 촌수계산

# 입력 값 받기
n = int(input())                    # 사람의 수
a, b = map(int, input().split())    # 촌수를 계산해야 하는 두 사람 a, b
m = int(input())                    # 관계의 수

# 그래프 생성
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False] * (n+1)           # 방문한 노드 체크용

# dfs 함수
def dfs(v, cnt):
    global flag
    visited[v] = True
    
    if v == b:
        print(cnt)
        flag = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i, cnt+1)

flag = False                        # 찾았는지 못찾았는지 확인용 flag
dfs(a, 0)                           # dfs 호출

# false -> 찾지 못했다는 뜻이므로 -1 출력하고 종료
if flag == False:
    print('-1')