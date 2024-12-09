a, b = map(int, input().split())
li = [i for i in range(1,a+1)]
idx = 0
result = []
while li:
    idx += b-1
    if idx >= len(li):
        idx %= len(li)
    result.append(str(li.pop(idx)))

print("<", ", ".join(result), ">", sep="")