n, m = map(int, input().split())
listA = [list(map(int, input())) for _ in range(n)]
listB = [list(map(int, input())) for _ in range(n)]
total = 0

def change_func(listA, a, b):
    for i in range(a, a+3):
        for j in range(b, b+3):
            if listA[i][j] == 0:
                listA[i][j] = 1
            else:
                listA[i][j] = 0
if n >= 3 or m >= 3:
    for i in range(n-2):
        for j in range(m-2):
            if listA[i][j] != listB[i][j]:
                change_func(listA, i, j)
                total += 1

    if listA == listB:
        print(total)
    else:
        print('-1')
else:
    if listA == listB:
        print('0')
    else:
        print('-1')