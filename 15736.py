n = int(input())
an = 0
for i in range(1, n+1):
    if i ** 2 <= n:
        an += 1
    else:
        break
print(an)

#for문을 사용하지 않고
an = int(n**(0.5)) #루트 취한것에 정수형만 받으면 제곱수의 개수를 구할 수 있다.
print(an)