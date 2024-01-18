N = int(input())
li = list(map(int, input().split()))
M = int(input())
li2 = list(map(int, input().split()))

dic = {}
for i in li:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in li2:
    if dic.get(i) == None:
        print(0, end=' ')
    else:
        print(dic.get(i), end=' ')