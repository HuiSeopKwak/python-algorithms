# [S/W 문제해결 기본] 2일차 - Sum

test_case = int(input())
max_sum = 0
li = [list(map(int, input().split())) for _ in range(100)]
row_sum, col_sum = 0, 0
for i in range(100):
    for j in range(100):
        row_sum += li[i][j]
        col_sum += li[j][i]
    if row_sum >= max_sum:
        max_sum = row_sum
    if col_sum >= max_sum:
        max_sum = col_sum
    row_sum = 0
    col_sum = 0
print(max_sum)

## 대각선도 구해주면 끝