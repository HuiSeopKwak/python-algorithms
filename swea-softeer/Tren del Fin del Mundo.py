N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key = lambda x: x[1])

print(li[0][0], li[0][1])