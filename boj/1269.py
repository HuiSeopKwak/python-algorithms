n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
dic = {}
cnt = 0

for i in arr1:
    dic[i] = 1
    
for i in arr2:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in dic:
    if dic[i] == 1:
        cnt += 1
print(cnt)

# 집합으로 풀리는데 그게 훨씬 간단하고 쉽네