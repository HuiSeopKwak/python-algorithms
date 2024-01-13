num, loc = map(int, input().split())
li = []
for i in range(1, num+1):
    if (num%i == 0):
        li.append(i)

if loc > len(li):
    print(0)
else:
    print(li[loc-1])
    
    


# N = int(input())
# li = list(map(int, input().split()))
# result = []
# li2 = [0]*N
# for i in range(N):
#     if li[i] not in result:
#         result.append(li[i])

# for i in range(N):
#     for j in range(len(result)):
#         if li[i] > result[j]:
#             li2[i] += 1
# for i in range(N):
#     print(li2[i], end=' ')