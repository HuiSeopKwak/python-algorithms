n = int(input())

li = [list(map(int, input().split())) for _ in range(n)]
li.sort(key = lambda x : (x[1],x[0]))   # 두개의 기주을 줘서 1번을 기준으로 정렬 한 뒤 겹치는 부분에 대해서 2번을 기준으로 다시 정렬해준다.
                                        # 만약 순서가 다르다면 sort를 두번해주는 방식으로 해주면 될듯
total = 1
end = li[0][1]

for i in range(1, n):
    if li[i][0] >= end:
        end = li[i][1]
        total += 1

print(total)