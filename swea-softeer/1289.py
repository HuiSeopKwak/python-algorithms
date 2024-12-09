# 원재의 메모리 복구하기 D3

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    goal_memory = list(map(int, input()))
    real_memory = [0 for _ in range(len(goal_memory))]
    length = len(goal_memory)
    cnt = 0

    for i in range(length):
        if goal_memory[i] != real_memory[i]:
            cnt += 1
            for j in range(i, length):
                if real_memory[j] == 0:
                    real_memory[j] = 1
                else:
                    real_memory[j] = 0
    print("#", test_case, " ", cnt, sep="")