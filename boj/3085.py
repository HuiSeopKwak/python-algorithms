n = int(input())

board = [list(input()) for _ in range(n)]
max_cnt = 0

def check():
    global max_cnt
    for i in range(n):
        cnt = 1
        for j in range(0,n-1):    #오른쪽 체크
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

        cnt = 1
        for j in range(0,n-1):    #아래쪽 체크
            if board[j][i] == board[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

for i in range(n):
    for j in range(n):
        if j < n-1:     # 오른쪽 교환
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            check()
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        if i < n-1:     # 아래쪽 교환
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            check()
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(max_cnt)