N = int(input())
li = list(map(int, input().split()))
M = int(input())
li2 = list(map(int, input().split()))

for i in li2:
    cnt = 0
    for j in li:
        if i == j:
            cnt += 1
    print(cnt, end=' ')
    
    
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
