T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    
    if k==0 or n==1:
        print(1)
    else:
        for j in range(k):
            for l in range(n):
                a=1