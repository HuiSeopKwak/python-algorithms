from collections import deque
case = int(input())
for i in range(case):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    cnt = 0
    while queue:
        biggest = max(queue)
        front = queue.popleft()
        m -= 1

        if front == biggest:
            cnt += 1
            if m < 0:
                print(cnt)
                break
        else:
            queue.append(front)
            if m < 0:
                m = len(queue) - 1