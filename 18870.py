N = int(input())
li = list(map(int, input().split()))
arr = sorted(set(li))
dic = {arr[i]:i for i in range(len(arr))}

for i in li:
    print(dic[i], end=" ")