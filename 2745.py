num,b = input().split()
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
an = 0
for i in range(0,len(num)):
    for j in range(len(number)):
        if num[i] == number[j]:
            an += j*(int(b)**(len(num)-(i+1)))
            
print(an)