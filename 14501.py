# 탑다운 dp를 이용해서 계산 중복을 없애주었음
def recur(day):
    global an
    
    if day == n:
        return 0
    if day > n:
        return -999999
    
    if dp[day] != -1:
        return dp[day]
    
    dp[day] = max(recur(day + consult[day][0]) + consult[day][1], recur(day+1))

    return dp[day]
        
n = int(input())

consult = [list(map(int, input().split())) for _ in range(n)]
dp = [-1 for _ in range(n)]

recur(0) #day, price

print(dp)


""" 재귀함수를 이용한 완전탐색방식(백트레킹)
def recur(day, price):
    global an
    
    if day == n:
        an = max(an, price)
        return
    if day > n:
        return
    
    recur(day + consult[day][0], price + consult[day][1])
    recur(day+1, price)
        
n = int(input())
  
consult = [list(map(int, input().split())) for _ in range(n)]
an = 0

recur(0, 0) #day, price

print(an)
"""