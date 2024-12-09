N = int(input())
an = []

while True:
    if N == 1:
        break
    else:
        for i in range(2, N+1):
            if N % i == 0:
                N = N // i
                an.append(i)
                break
            else:
                continue
for i in an:
    print(i)