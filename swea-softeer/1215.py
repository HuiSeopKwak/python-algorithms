# [S/W 문제해결 기본] 3일차 - 회문1 D3

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
"""
for test_case in range(1,11):
    n = int(input())
    table = [list(input()) for _ in range(8)]
    cnt = 0

    # 가로 확인
    for i in range(8):
        for j in range(8-n+1):
            if j == 0:
                if table[i][j:j+n] == table[i][j+n-1::-1]:
                    cnt += 1
            else:
                if table[i][j:j+n] == table[i][j+n-1:j-1:-1]:
                    cnt += 1

    # 가로 세로 변경
    for i in range(8):
        for j in range(i, 8):
            if i != j:
                temp = table[i][j]
                table[i][j] = table[j][i]
                table[j][i] = temp

    # 세로 확인
    for i in range(8):
        for j in range(8-n+1):
            if j == 0:
                if table[i][j:j+n] == table[i][j+n-1::-1]:
                    cnt += 1
            else:
                if table[i][j:j+n] == table[i][j+n-1:j-1:-1]:
                    cnt += 1

    print("#", test_case, " ", cnt, sep="")
    """

for c in range(1, 2):
    n = int(input())
    li = [input() for _ in range(8)]
    cnt = 0
    print(li)
    # 가로
    for i in range(8):
        for j in range(0, 8-n+1):
            sub = li[i][j:j+n]
            print(sub)
            if sub == sub[::-1]:
                cnt += 1

    # 세로
    for j in range(8):
        for i in range(0, 8-n+1):
            sub = []
            for q in range(n):
                sub.append(li[i+q][j])
                # print('before', sub)
            sub = ''.join(sub)
            # print('after', sub)
            # print('::-1', sub[::-1])
            if sub == sub[::-1]:
                cnt += 1

    print(f'#{c} {cnt}')