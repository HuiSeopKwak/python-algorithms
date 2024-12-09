bag, num = map(int, input().split())

value = [list(map(int, input().split())) for _ in range(num)]

dp = [0] * (bag + 1)

for i in range(num):
    weight, price = value[i]
    for j in range(bag, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + price)

print(dp[bag])
