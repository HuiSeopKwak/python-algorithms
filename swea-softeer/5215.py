# 햄버거 다이어트 D3

def recur(idx, taste, cal):
    global max_taste
    if max_taste < taste and cal <= l:
        max_taste = taste
    if idx == n or cal > l:
        return 
    # 인덱스 재료 넣는 경우
    recur(idx + 1, taste + li[idx][0], cal + li[idx][1])
    # 인덱스 재료 안 넣는 경우
    recur(idx + 1, taste, cal)
    

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, l = map(int, input().split()) # n : 재료의 개수, l : 최대 칼로리
    li = [list(map(int, input().split())) for _ in range(n)] # [0]: 재료의 맛, [1] : 칼로리
    max_taste = 0
    recur(0, 0, 0)
    print("#", test_case, " ", max_taste, sep="")