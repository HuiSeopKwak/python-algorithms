import sys
n, m = map(int, sys.stdin.readline().split())

room = [input() for _ in range(n)]
reserved = [list(map(str, input().split())) for _ in range(m)]
print(room)
print(reserved)
print(sorted(reserved))

# for i in range(n):
#     for j in range(m):
#         if room[i] == reserved[j][0]:

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ing