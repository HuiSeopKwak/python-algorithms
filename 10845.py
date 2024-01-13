import sys
queue = []
operator = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push':
        queue.append(command[1])
    elif command[0] == 'front':
        if queue:
            operator.append(queue[0])
        else:
            operator.append('-1')
    elif command[0] == 'back':
        if queue:
            operator.append(queue[-1])
        else:
            operator.append('-1')
    elif command[0] == 'empty':
        if queue:
            operator.append('0')
        else:
            operator.append('1')
    elif command[0] == 'pop':
        if queue:
            operator.append(queue.pop(0))
        else:
            operator.append('-1')
    else:   #size
        operator.append(len(queue))

for i in operator:
    print(i)