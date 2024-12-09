n, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))

s, e = 0, len(arr)-1
cnt = 0
remain = 0

while s <= e:
    if arr[e] == x:
        cnt += 1
        e -= 1
        continue

    if s == e:
        remain += 1
        break

    if arr[s] + arr[e] >= x/2:
        cnt += 1
        s += 1
        e -= 1
    else:
        s += 1
        remain += 1
# 0ml 가 든 병이던, remain으로 분류된 병들은 3개가 모인다면 하나의 다찬 병을 알아낼 수 있다. 즉 -> remain // 3은 더 추가할 수 있는 full병의 개수
print(cnt + (remain//3))