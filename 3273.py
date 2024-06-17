n = int(input())
nums = list(map(int, input().split()))
k = int(input())
nums.sort()

start, end = 0, len(nums)-1
cnt = 0
# 투 포인터 이용
# 정렬 후 왼쪽 오른쪽에서 하나씩 움직이면서 가능성 없는 수는 탐색 안하는 방향으로 복잡도를 낮춤
while start != end:
    if nums[start] + nums[end] > k:
        end -= 1
    elif nums[start] + nums[end] < k:
        start += 1
    elif nums[start] + nums[end] == k:
        cnt += 1
        end -= 1

print(cnt)