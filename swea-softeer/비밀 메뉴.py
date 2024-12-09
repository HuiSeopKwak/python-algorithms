M, N, K = map(int, input().split())
secret = list(map(int, input().split()))
num = list(map(int, input().split()))
stack = []
menu = False

for i in num:
    stack.append(i)
    if stack[len(stack)-M:len(stack)] == secret:
        menu = True
if menu == True:
    print('secret')
else:
    print('normal')