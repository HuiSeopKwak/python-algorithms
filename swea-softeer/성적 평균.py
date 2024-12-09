student, case = map(int, input().split())

score = list(map(int, input().split()))
result = []
for i in range(case):
    a, b = map(int, input().split())
    sum = 0
    for j in range(a-1,b):
        sum += score[j]
    sum = sum / (b-a+1) 
    result.append(round(sum,2))

for i in result:
    print('{:.2f}'.format(i))