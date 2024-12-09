# 초심자의 회문 검사 D2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    string = input()
    check = False
    re_string = string[::-1]

    if string == re_string:
        check = True

    if check == False:
        print("#", test_case, " 0", sep="")
    else:
        print("#", test_case, " 1", sep="")