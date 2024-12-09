# 숫자 배열 회전 D2

def check(X, Y):
    # X의 길이가 항상 Y보다 짧거나 같다
    global max_sum
    for i in range(len(Y)-len(X)+1):
        sum = 0
        for j in range(len(X)):
            sum += X[j]*Y[i+j]
        if sum > max_sum:
            max_sum = sum

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    max_sum = 0
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if n >= m:
        check(B, A)
    else:
        check(A, B)
    print("#", test_case, " ", max_sum, sep="")