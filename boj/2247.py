n = int(input())

csod = 0

for i in range(2, n//2+1):
    csod += ((n//i - 1)*i) % 1000000    # i 숫자 본인은 약수가 안되기 때문에 1씩 빼주면서 더해줘야 한다.

print(csod % 1000000)