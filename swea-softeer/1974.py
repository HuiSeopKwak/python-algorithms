# 스도쿠 검증 D2

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    li = [list(map(int, input().split())) for _ in range(9)]
    nums = [0]*10
    check = True
    # 가로 확인
    for i in range(9):
        for j in range(9):
            nums[li[i][j]] += 1
        if nums[1] == nums[2] == nums[3] == nums[4] == nums[5] == nums[6] == nums[7] == nums[8] == nums[9]:
            continue
        else:
            print("#", test_case, " 0", sep="")
            check = False
            break
    # 세로 확인
    if check == True:
        for i in range(9):
            for j in range(9):
                nums[li[j][i]] += 1
            if nums[1] == nums[2] == nums[3] == nums[4] == nums[5] == nums[6] == nums[7] == nums[8] == nums[9]:
                continue
            else:
                print("#", test_case, " 0", sep="")
                check = False
                break

    # 3*3 확인
    if check == True:
        for i in range(0, 8, 3):
            for j in range(0, 8, 3):
                nums[li[i][j]] += 1
                nums[li[i][j+1]] += 1
                nums[li[i][j+2]] += 1
                nums[li[i+1][j]] += 1
                nums[li[i+1][j+1]] += 1
                nums[li[i+1][j+2]] += 1
                nums[li[i+2][j]] += 1
                nums[li[i+2][j+1]] += 1
                nums[li[i+2][j+2]] += 1
                if nums[1] == nums[2] == nums[3] == nums[4] == nums[5] == nums[6] == nums[7] == nums[8] == nums[9]:
                    continue
                else:
                    print("#", test_case, " 0", sep="")
                    check = False
                    break
            if check == False:
                break
    if check == True:
        print("#", test_case, " 1", sep="")