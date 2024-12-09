e, s, m = map(int, input().split())
e = e % 15
s = s % 28
m = m % 19
i = 1
while 1:
    if i % 15 == e:
        if i % 28 == s:
            if i % 19 == m:
                break
    i += 1
print(i)