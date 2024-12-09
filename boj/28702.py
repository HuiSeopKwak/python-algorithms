goal_num = 0

for i in range(3):
    a = input()
    if a.isdigit() == True:
        goal_num = int(a) + (3 - i) # 목표 숫자 찾기
if goal_num % 3 == 0 and goal_num % 5 == 0:
    print('FizzBuzz')
elif goal_num % 3 == 0:
    print('Fizz')
elif goal_num % 5 == 0:
    print('Buzz')
else:
    print(goal_num)