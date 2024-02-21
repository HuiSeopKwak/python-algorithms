def check(candy):
    print(candy)


candy = []
N = int(input())
candy= [list(input()) for _ in range(N)]
print(candy)
print(candy[1][1])

for i in range(N):
    for j in range(N):
        # 오른쪽 교환
        if j+1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            check(candy)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] #원상 복구
        
        # 아래쪽 교환
        if i+i < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            check(candy)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j] #원상 복구