import sys
input = sys.stdin.readline

max_width, max_height, min_width, min_height = -500001, -500001, 500001, 500001
shape = []

n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    if x > max_width:
        max_width = x
    elif x < min_width:
        min_width = x

    if y > max_height:
        max_height = y
    elif y < min_height:
        min_height = y

    shape.append([x, y])

width = [0 for _ in range(min_width, max_width+1)]
height = [0 for _ in range(min_height, max_height+1)]

for i in range(n):
    width[shape[i][0]] += 1

    ################## 쉽지 않네