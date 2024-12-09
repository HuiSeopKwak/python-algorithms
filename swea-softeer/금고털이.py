bag, num = map(int, input().split())
maxprice = 0
weight = 0

price = [0]*10001
for i in range(num):
    a, b = map(int, input().split())
    price[b] = price[b] + a
# 하 같은 price 이지만 다른 금속인 애들에 대한 경우를 안더해줬음
# 그냥 price[b] 하면 안되고 원래 있는 price에 더하기 a 를 해야줘야한데
# 아오 시발 왤케 짜증나게 만들었냐
for i in range(len(price)-1, 0, -1):
    if price[i] != 0:
        maxprice += price[i] * i
        weight += price[i]
    if weight > bag:
        cut = weight - bag
        maxprice -= cut * i
        break
print(maxprice)