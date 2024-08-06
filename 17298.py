N = int(input())
li = list(map(int, input().split()))
stack = [0]
an = [-1]*N

for i in range(1, N):
    while stack and li[stack[-1]] < li[i]:
        an[stack.pop()] = li[i]
    stack.append(i)

for i in an:
    print(i, end=' ')