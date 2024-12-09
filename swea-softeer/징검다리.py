n = int(input())
rock = list(map(int, input().split()))
result = [1]*n

for i in range(1, n):
    for j in range(1, i):
        if rock[j] < rock[i]:
            result[i] += 1

print(max(result))

# 아오 쉬운거 같은데 은근 복잡하네 머리가 안돌아가서 그런가...ㅠㅠ