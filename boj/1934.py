T = int(input())
an = []
for i in range(T):
    a, b = map(int, input().split())
    a1, b1 = a, b
    while a1 > 0:
        b1, a1 = a1, b1 % a1
    an.append(int((a*b)/b1))

for i in an:
    print(i)