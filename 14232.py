n = int(input())
a = 0
b = 0
# n까지 할 필요 없고 n의 제곱근 까지만 확인하면 약수의 모든 경우를 찾을 수 있다. -> 그 안에 아무것도 없다면 소수인것

for i in range(2, int(n**(0.5)+1)):
    if n % i == 0:
        if a + b < i + (n//i):
            a, b = i, n//i
    
print(2)
print(a, b)