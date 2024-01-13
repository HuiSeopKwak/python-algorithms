from collections import deque
import sys
lideque = deque()
operator = []

for _ in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        lideque.appendleft(command[1])
    elif command[0] == 'push_back':
        lideque.append(command[1])
    elif command[0] == 'pop_front':
        if lideque:
            operator.append(lideque.popleft())
        else:
            operator.append('-1')
    elif command[0] == 'pop_back':
        if lideque:
            operator.append(lideque.pop())
        else:
            operator.append('-1')
    elif command[0] == 'size':
        operator.append(len(lideque))
    elif command[0] == 'empty':
        if lideque:
            operator.append('0')
        else:
            operator.append('1')
        
    elif command[0] == 'front':
        if lideque:
            operator.append(lideque[0])
        else:
            operator.append('-1')
    else:   #back
        if lideque:
            operator.append(lideque[-1])
        else:
            operator.append('-1')

for i in operator:
    print(i)