li = []
an = []
for i in range(9):
    li.append(int(input()))

for i in range(9):
    for j in range(9):
        if i == j:
            continue
        if sum(li) - li[i] - li[j] == 100:
            an = li.copy()
            if i>j:
                an.pop(i), an.pop(j)
            else:
                an.pop(j), an.pop(i)

for i in sorted(an):
    print(i)