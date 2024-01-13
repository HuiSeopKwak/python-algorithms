N = int(input())
li = list(map(int, input().split()))
M = int(input())
li2 = list(map(int, input().split()))

for i in li2:
    cnt = 0
    for j in li:
        if i == j:
            cnt += 1
    print(cnt, end=' ')