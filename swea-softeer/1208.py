# [S/W 문제해결 기본] 1일차 - Flatten

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    box = list(map(int, input().split()))

    for i in range(n):
        max_index = box.index(max(box))
        min_index = box.index(min(box))
        box[max_index] -= 1
        box[min_index] += 1

    print("#", test_case, " ", max(box) - min(box), sep="")