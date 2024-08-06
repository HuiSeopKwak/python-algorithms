n, m = map(int, input().split())

monster = list(input() for _ in range(n))
test = list(input() for _ in range(m))
dicmonster = {}
i = 0
for name in monster:
    i += 1
    dicmonster[i] = name
    dicmonster[name] = i

for j in test:
    if j.isdigit():
        print(dicmonster[int(j)])
    else:
        print(dicmonster[j])