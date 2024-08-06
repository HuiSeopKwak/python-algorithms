n, k = map(int, input().split())
li = [i for i in range(1, n+1)]
cnt = 0
answer = []

while li:
    cnt += k-1
    if len(li) <= cnt:
        cnt = cnt%len(li)
    
    answer.append(str(li.pop(cnt)))

print("<",", ".join(answer),">", sep='')