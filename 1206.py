T = 10
for test_case in range(1, T+1):
    answer = 0
    building = int(input())
    height = list(map(int, input().split()))

    for count in range(2,building-1):
        maxheight = 0
        if height[count] > height[count-1] and height[count] > height[count-2]:
            if height[count] > height[count+1] and height[count] > height[count+2]:
                maxheight = height[count] - max(height[count-1], height[count-2], height[count+1], height[count+2])
        
        answer += maxheight

    print(f"#{test_case} {answer}")