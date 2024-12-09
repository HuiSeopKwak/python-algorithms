# 파리퇴치

import sys
input = sys.stdin.readline

def check():
    m_sum = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for y in range(m):
                for x in range(m):
                    sum += bugs[i+y][j+x]
            m_sum = max(sum, m_sum)

    return m_sum
T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    max_sum = 0
    bugs = [list(map(int, input().split())) for _ in range(n)]
    

    max_sum = check()
    print("#", test_case ," ", max_sum, sep="")