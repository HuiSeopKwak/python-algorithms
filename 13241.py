a, b = map(int, input().split())
a1, b1 = a, b
while a1 > 0:
    b1, a1 = a1, b1 % a1


print(int((a*b)/b1))



# 최대공약수, 최소공배수 구할때


# print(a1) 최대공약수
# print(int((a*b)/a1)) 최소공배수
