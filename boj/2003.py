n, m = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
left, right = 0, 1

while right <= n and left <= right:
    part = arr[left:right]
    sum_arr = sum(part)

    if sum_arr == m:
        cnt += 1
        right += 1
    elif sum_arr >= m:
        left += 1
    else:
        right += 1

print(cnt)