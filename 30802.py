import math
N = int(input())    # 참가자 수
size = list(map(int, input().split()))  # 0, 1, 2, 3, 4, 5 사이즈 별 참가자 수
T, P = map(int, input().split())    # 티셔츠 묶음, 펜 묶음 개수

total_T = 0 # 총 티셔츠 묶음 개수

for i in range(6):  # 총 티셔츠 묶음 개수 구하기
    total_T += math.ceil(size[i]/T) 

print(total_T)
print(int(N/P), N - P*int(N/P))