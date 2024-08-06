def check(a):
    global minimum
    b = []  #link 팀
    # link 팀에 멤버 추가
    for i in range(len(line)):
        if i not in a:
            b.append(i)
    start, link = 0, 0

    #start team 점수
    for i in a:
        for j in a:
            start += li[i][j]
    #link team 점수
    for i in b:
        for j in b:
            link += li[i][j]

    if abs(start - link) <= minimum:
        minimum = abs(start - link)
            
def select(idx, cnt):
    global arr
    if cnt == n//2: # a 팀 인원이 절반이 될때
        if arr[0] == line[0]: # 1번이 들어가는 경우만 고려해주면 정확히 전체의 절반(필요한 경우만 계산가능)
            check(arr)
        return
    else:
        if idx == n:
            return
        arr.append(line[idx])
        select(idx + 1, cnt + 1)
        arr.pop()
        select(idx + 1, cnt)
        
n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
# 계산할 애들 뽑기 위한 리스트 
line = [i for i in range(n)]
minimum = 1_000_000_000
# 계산할 한팀 수정용 리스트
arr = []

select(0, 0)

print(minimum)