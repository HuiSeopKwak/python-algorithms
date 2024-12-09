import sys

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
count = [0]*1000001
stack =[0]
an = [-1]*N
for i in li:
    count[i] += 1

for i in range(1, N):
    while stack and count[li[stack[-1]]] < count[li[i]]:
        an[stack.pop()] = li[i]
    stack.append(i)

print(" ".join(map(str, an)))