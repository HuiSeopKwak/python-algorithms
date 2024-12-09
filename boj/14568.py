n = int(input())
ans = 0

for taek in range(1,n):
    for nam in range(1,n):
        for young in range(1,n):
            if taek + nam + young == n:
                if nam >= young + 2:
                    if taek % 2 != 1:
                        ans += 1
print(ans)