import sys
input = sys.stdin.readline
n, m = map(int, input().split())
trees = list(map(int, input().split()))

s = 0
e = max(trees)

while s <= e:
    wood = 0    
    mid = (s + e)//2
    for tree in trees:
        if tree > mid:
            wood += tree - mid
    if wood < m:
        e = mid - 1
    elif wood >= m:
        s = mid + 1

print(e)