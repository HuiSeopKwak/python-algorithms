N = int(input())
li = list(map(int, input().split()))
arr = sorted(set(li))
dic = {arr[i]:1 for i in range(len(arr))}
M = int(input())
li2 = list(map(int, input().split()))
for i in range(len(li2)):
    if li2[i] in dic:
        print(1)
    else:
        print(0)