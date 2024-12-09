#백만장자 프로젝트

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m = int(input())
    arr = list(map(int, input().split()))
    sellprice = 0
    an = 0

    for i in arr[::-1]:
        if i > sellprice:
            sellprice = i
        else:
            an += sellprice - i
    
    
    print("#", test_case, " ", an, sep="")