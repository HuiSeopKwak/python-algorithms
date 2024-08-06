import sys
repeat = int(sys.stdin.readline())

for i in range(repeat):
    word = sys.stdin.readline().split()
    for i in word:
        for j in range(len(i)):
            print(i[len(i)-j-1], end='')
        print(' ', end='')
    print()
    

# N = int(input())

# for i in range(N):
#     string=list(input().split())
#     for j in string:
#         print(j[::-1], end=' ')