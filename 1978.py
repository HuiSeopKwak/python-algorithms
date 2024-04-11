count = int(input())
numlist = list(map(int, input().split()))
solo = 0

for i in numlist:
    error = 0
    if i > 1:
        for j in range(2, int(i**(0.5))+1): 
            if (i%j) == 0:
                error += 1
        if error == 0:
            solo += 1
print(solo)