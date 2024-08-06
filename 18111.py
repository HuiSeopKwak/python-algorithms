# import sys
# n, m, b = map(int, sys.stdin.readline().split())
# ground = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
# an = 100000000       # 시간
# ground_an = 0
# for i in range(257): # 땅 높이
#     use_block, take_block = 0, 0
#     for j in range(n):
#         for k in range(m):
#             if ground[j][k] > i:
#                 take_block += ground[j][k] - i
#             else:
#                 use_block += i - ground[j][k]

#     if use_block > take_block + b:
#         continue

#     time = take_block * 2 + use_block

#     if time <= an:
#         an = time
#         ground_an = i

# print(an, ground_an)

# import sys

# n, m, b = map(int, sys.stdin.readline().split())
# ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# an = sys.maxsize
# ground_an = 0

# for i in range(257):
#     take_block, use_block = 0, 0

#     for j in range(n):
#         for k in range(m):

#             if ground[j][k] > i:
#                 take_block += ground[j][k] - i
#             else: 
#                 use_block += i - ground[j][k]
#     if take_block + b >= use_block:
#         if (take_block * 2) + use_block <= an:
#             an = (take_block * 2) + use_block
#             ground_an = i

# print(an, ground_an)

import sys
n, m, b = map(int,input().split())
block = []
for _ in range(n):
    block.append([int(x) for x in sys.stdin.readline().rstrip().split()])
an = int(1e9)
ground_an = 0

for i in range(257): #땅 높이
    use_block = 0
    take_block = 0
    for x in range(n):
        for y in range(m):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]

    if use_block > take_block + b:
        continue
    count = take_block * 2 + use_block
    if count <= an:
        an = count
        ground_an = i
print(an, ground_an)