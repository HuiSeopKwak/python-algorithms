string = list(input())
bomb = list(input())
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if stack[len(stack)-len(bomb):len(stack)] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))