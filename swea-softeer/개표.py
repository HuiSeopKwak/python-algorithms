import sys

T = int(input())
N = [0]*T
for i in range(T):
    N[i] = int(sys.stdin.readline())

for i in N:
    if i/5 > 0:
        for j in range(int(i/5)):
            print('++++ ', end='')
    for k in range(i%5):
        print('|', end='')
    print()