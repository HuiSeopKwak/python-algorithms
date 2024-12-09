N = int(input()) # total num
li = []
result = []
temp = True
cnt = 1
for i in range(1, N+1):
    num = int(input())
    while num >= cnt:
        li.append(cnt)
        cnt += 1
        result.append('+')
    if num == li[-1]:
        result.append('-')
        li.pop()
    else:
        temp = False
        break

if temp == False:
    print("NO")
else:
    for i in result:
        print(i)