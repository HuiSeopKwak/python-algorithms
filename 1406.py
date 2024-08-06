# 참고 코드
import sys

st1 = list(sys.stdin.readline().rstrip())
st2 =[]

for i in range(int(sys.stdin.readline())):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if st1:
            st2.append(st1.pop())
            
    elif command[0] == 'D':
        if st2:
            st1.append(st2.pop())
    
    elif command[0] == 'B':
        if st1:
            st1.pop()
    
    else:
        st1.append(command[1])
        
st1.extend(reversed(st2))
print(''.join(st1))

# import sys
# string = list(input())
# N = int(sys.stdin.readline())
# cursor = len(string)

# for i in range(N):
#     command = sys.stdin.readline().split()
#     if command[0] == 'L':
#         if cursor == 0:
#             pass
#         else:
#             cursor -= 1
#     elif command[0] == 'D':
#         if cursor == len(string):
#             pass
#         else:
#             cursor += 1
#     elif command[0] == 'B':
#         if cursor == 0:
#             pass
#         else:
#             del string[cursor-1]
#             cursor -= 1
            
#     elif command[0] == 'P':
#         string.insert(cursor ,command[1])
#         cursor += 1
    
# for i in string:
#     print(i, end='')