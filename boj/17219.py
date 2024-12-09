import sys
n, m = map(int, sys.stdin.readline().split())
dic ={}
an =[]

for i in range(n):
    url, password = map(str, sys.stdin.readline().split())
    dic[url] = password

for i in range(m):
    url = sys.stdin.readline().rstrip()
    if url in dic:
        an.append(dic[url])

for i in an:
    print(i)