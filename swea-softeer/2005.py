# 파스칼의 삼각형 D2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n = int(input())
    li = [[0 for _ in range(n+1)] for _ in range(n+1)]
    li[1][1] = 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            li[i][j] = li[i-1][j] + li[i-1][j-1]
    
    print("#", test_case, sep="")
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(li[i][j], end = " ")
        print()