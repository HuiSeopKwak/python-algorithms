# 끝자리가 0이라는 것은 2 와 5의 곱으로 이루어 졌으면 0이 된다.
# 만약 xxxxx00 이면 2가 2개 5가 2개의 곱으로 이루어 졌다는 것이다.
# 즉, 2, 5의 쌍을 구하면 0의 개수를 구할 수 있다.

n, m = map(int, input().split())


def two_count(a):
    two = 0
    while a != 0:
        a = a // 2  #1~a 까지 2의 배수 개수
        two += a
    return two

def five_count(b):
    five = 0
    while b != 0:
        b = b // 5
        five += b
    return five

tcnt = two_count(n) - two_count(n-m) - two_count(m) # 2의 개수
fcnt = five_count(n) - five_count(n-m) - five_count(m) # 5의 개수

print(min(tcnt, fcnt)) # 둘 중 적은 값으로 출력 (2와 5의 쌍으로 구성되어야 10이 되기 때문에 적은 값이 0의 개수이다)