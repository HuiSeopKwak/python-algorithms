n = int(input())
card = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

for number in find:
    start = 0
    end = n-1
    flag = False
    
    while start <= end:
        mid = (start + end) // 2
        if card[mid] == number:
            print('1', end =' ')
            flag = True
            break
        elif card[mid] < number:
            start = mid + 1
        else:
            end = mid - 1
    if flag == True:
        continue
    else:
        print('0', end=' ')