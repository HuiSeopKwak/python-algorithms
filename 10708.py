n = int(input()) # 사람 수
k = int(input()) # 게임 반복 수
arr = list(map(int, input().split())) # 게임 당 타겟 번호
score = [0]*(n+1)

for i in range(k):
    picked = list(map(int, input().split()))
    cnt = 0
    for j in range(n):
        if picked[j] == arr[i]:
            score[j] += 1
        else:
            cnt += 1
    score[arr[i]-1] += cnt
for i in range(n):
    print(score[i])