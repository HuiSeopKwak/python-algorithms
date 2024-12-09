while(True):
    sentence =input()
    if sentence == '.':
        break
    
    result = True
    stack = []
    for i in sentence:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                result = False 
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                result = False
                break

    if len(stack) == 0 and result == True:
        print('yes')
    else:
        print('no')