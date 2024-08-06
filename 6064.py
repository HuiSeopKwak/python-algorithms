# t = int(input())

# li = [list(map(int, input().split())) for _ in range(t)]
# for i in range(t):
#     check = False
#     n = li[i][0]
#     m = li[i][1]
#     x = li[i][2]
#     y = li[i][3]
#     k = x
#     while k <= n*m:
#         if (k-x) % n == 0 and (k-y) % m == 0:
#             print(k)
#             check = True
#             break
#         k += n
        
#     if check == False:
#         print('-1')
#     else:
#         continue


import sys


def calculate(m, n, x, y):
    k = x #k를 x로 초기화
    while k <= m * n: #k의 범위는 m*n을 넘을 수 없기에
        if (k - x) % m == 0 and (k - y) % n == 0: #2개의 조건을 만족하는 k값을 찾는다.
            return k
        k += m #k-x가 m의 배수이기 때문에 k는 x로 초기화해주었기 때문에 m만 더해준다.
    return -1


t = int(input())

for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())

    print(calculate(m, n, x, y))