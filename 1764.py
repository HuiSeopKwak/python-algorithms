import sys
n, m = map(int, sys.stdin.readline().split())
dic = {}
an = []
for i in range(1,n+1):
    name = sys.stdin.readline().rstrip()
    dic[name] = i

for i in range(m):
    name = sys.stdin.readline().rstrip()
    if name in dic:
        an.append(name)
an.sort()
print(len(an))
for i in an:
    print(i)