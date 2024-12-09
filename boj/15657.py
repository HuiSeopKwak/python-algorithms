def recur(number):
    if number == m:     #맞는 개수만큼 호출되었을때 프린트
        print(*arr)
        return
    
    for i in li:
        if len(arr) > 0 and i < max(arr):
            continue
        arr.append(i)
        recur(number+1) #number가 재귀 호출 되는 개수 나타내는 것
        arr.pop()

n, m  = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
arr = []

recur(0)