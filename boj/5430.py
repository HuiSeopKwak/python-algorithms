import re

t = int(input())
for _ in range(t):
    check = True    # 에러 시 출력 막기용
    reverse_cnt = 0 # 매번 reverse 시키지 않고 모든 연산 끝난 후 pop하기 위해 짝수인지 홀수인지 확인용 count
    p = input()
    n = int(input())
    arr = input()
    arr = re.findall(r'\d+', arr)   # 숫자만 추출해주는 코드
    # arr = list(map(int, arr))     # 정수형으로 바꿔주는 코드
    
    for i in p:
        if i == 'R':
             reverse_cnt += 1
        else:   # i == 'D'
            if len(arr) != 0:
                if reverse_cnt % 2 == 0:    # 짝수면
                    arr.pop(0)
                else:   # 홀수면
                    arr.pop(-1)
            else:
                print('error')
                check = False
                break
    
    if reverse_cnt % 2 == 1:    # 홀수 일때만 reverse 해줌
         arr = list(reversed(arr))
    if check == True:
        print('[' + ','.join(arr) + ']')