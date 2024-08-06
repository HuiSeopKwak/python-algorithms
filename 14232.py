n = int(input())
an = []
# n까지 할 필요 없고 n의 제곱근 까지만 확인하면 약수의 모든 경우를 찾을 수 있다. -> 그 안에 아무것도 없다면 소수인것

for i in range(2, int(n**(0.5)+1)):
    while n % i == 0:
        an.append(i)
        n = n // i
        
if n != 1:  # 끝까지 1이 되지 않았다면 마지막 수 append
    an.append(n)

print(len(an))
print(*an)