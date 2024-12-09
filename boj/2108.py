import sys
from collections import Counter # 최빈값용
def cal(num):           # 반올림 함수
    if num > 0:
        if num - int(num) >= 0.5:
            num = int(num)+1    
        return int(num)

    if num < 0:
        if abs(num - int(num)) >= 0.5:
            num = int(num)-1
        return int(num)

n = int(input())
li = []
for i in range(n):
    li.append(int(sys.stdin.readline()))
li.sort()

print(round(sum(li)/n))
print(li[int(len(li)/2)])
count_li = Counter(li).most_common()
if len(count_li) > 1 and count_li[0][1] == count_li[1][1]:
    print(count_li[1][0])
else:
    print(count_li[0][0])
print(max(li) - min(li))