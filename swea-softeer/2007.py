# 패턴 마디의 길이 D2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    length = 0

    for i in range(1,10):
        if string[0:i] == string[i:2*i]:
            length = i
            break
    print("#", test_case, " ", length, sep="")