n, s = map(int, input().split())
li = list(map(int, input().split()))
arr = []

def gcd(x, y): #gcd = 최대공약수, math 라이브러리에서 math.gcd()와 같은 함수
    if y > x:
        x, y = y, x
    while y>0:
        x, y = y, x % y
    return x

for i in li:
    arr.append(abs(s - i))

an = arr[0]

for i in range(1, n):
    an = gcd(arr[i], an)

print(an)