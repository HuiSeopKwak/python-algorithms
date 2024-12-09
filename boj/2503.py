n = int(input())

hint = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if (a == b or b == c or c == a):
                continue
            cnt = 0
            for arr in hint:
                number = arr[0]
                strike = arr[1]
                ball = arr[2]
            
                ball_count = 0  
                strike_count = 0    

                number = str(number)
                if str(a) == number[0]:
                    strike_count += 1
                elif str(a) == number[1] or str(a) == number[2]:
                    ball_count += 1
                if str(b) == number[1]:
                    strike_count += 1
                elif str(b) == number[0] or str(b) == number[2]:
                    ball_count += 1
                if str(c) == number[2]:
                    strike_count += 1
                elif str(c) == number[0] or str(c) == number[1]:
                    ball_count += 1

                if strike_count == strike and ball_count == ball:
                    cnt += 1
                
            if cnt == n:
                answer += 1
print(answer)