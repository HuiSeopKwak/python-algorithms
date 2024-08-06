import sys
n = int(sys.stdin.readline().rstrip())
array = set()

for _ in range(n):
    li = sys.stdin.readline().split()
    if len(li)==1:
        if li[0] == 'all':
            array = set([i for i in range(1, 21)])
        else:
            array = set()
    else:
        func, value = li[0], int(li[1])
        if func == 'add':
            array.add(value)
        elif func == 'remove':
            array.discard(value)
        elif func == 'check':
            if value in array:
                print('1')
            else:
                print('0')
        elif func == 'toggle':
            if value in array:
                array.discard(value)
            else:
                array.add(value)