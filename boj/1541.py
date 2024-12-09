str = input()
str1 = str.split('-')
min_sum = 0
check = True

for i in str1:
    a = i.split('+')
    if check == True:
        for i in a:
            min_sum += int(i)
        check = False
    else:
        for i in a:
            min_sum -= int(i)
                        
print(min_sum)