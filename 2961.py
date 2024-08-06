def recur(index, s, b, use):
    global an

    if index == n:
        if use != 0:
            an = min(an, abs(s-b)) 
        return       

    recur(index+1, s*li[index][0], b+li[index][1], use+1)  # 재료 사용하는 경우
    recur(index+1, s, b, use)                            # 재료 사용안하는 경우

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]
an = 9999999999
if n > 1:
    recur(0, 1, 0, 0) # index, 신맛, 쓴맛 신맛의 경우 곱하기를 해야하기 때문에 1로 시작한다, + 0개 사용경우 제외 위한 4번째 패러미터
else:
    an = abs(li[0][0]-li[0][1])

print(an)