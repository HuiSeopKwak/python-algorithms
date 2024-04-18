import sys
input = sys.stdin.readline

def recur(idx, p, f, s, v, c, use):
    global an, standard, anuse
    str1, str2 = '', ''
    if idx == n:
        if p >= standard[0] and f >= standard[1] and s >= standard[2] and v >= standard[3]:
            if an > c:
                an = c
                anuse = use.copy()
            elif an == c:                   # 최소값 같을떼 문자열 사전순 비교하는 부분
                for i in range(len(anuse)):
                    if anuse[i] > 0:
                        str1 = str1 + str(i+1)
                for i in range(len(use)):
                    if use[i] > 0:
                        str2 = str2 + str(i+1)
                if str2 < str1:
                    anuse = use.copy()
                    
        return

    use[idx] = 1
    recur(idx+1, p+nut[idx][0], f+nut[idx][1], s+nut[idx][2], v+nut[idx][3], c+nut[idx][4], use)
    use[idx] = 0
    recur(idx+1, p, f, s, v, c, use)


n = int(input())
standard = list(map(int, input().split()))
nut = [list(map(int, input().split())) for _ in range(n)]
an = 999999999
use = [0 for _ in range(n)]
recur(0, 0, 0, 0, 0, 0, use)

if an != 999999999:
    print(an)
    for i in range(len(anuse)):
        if anuse[i] > 0:
            print(i+1, end=" ")
else:
    print('-1')

# 사전순으로 가장 빠른 것을 찾아야하는데
# use 배열을 사용해서 답을 구하려니 사전 순으로 비교하기가 힘들다
# 그래서 다른 방식으로 어떤 것을 썼는지 기록 하고 사전 순 비교를 하던지
# 아니면 그냥 use를 크거나 같을때 사전으로 변환후 확인해서(같을때는 사전 순 확인 용)
# 더 사전순으로 앞서 있는 것을 저장해두는 것이 괜찮을지도?
# 둘 중 하나 선택해서 다시 풀어보자
# use 말고 배열 사용해서 사용되는 index append , pop 한 후에 그것을 사전 순 확인?