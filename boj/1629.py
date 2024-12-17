a, b, c = map(int, input().split())

def multi(a1, b1):
    if b1 == 1:
        return a1 % c
    else:
        tmp = multi(a1, b1 // 2)
        if b1 % 2 == 0:  # 짝수면
            return (tmp * tmp) % c
        else:  # 홀수면
            return (tmp * tmp * a1) % c

print(multi(a, b))