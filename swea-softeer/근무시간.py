sum = 0
for i in range(5):
    a = list(input())

    start = (int(a[0])*10+int(a[1]))*60 + int(a[3])*10+int(a[4])
    end = (int(a[6])*10+int(a[7]))*60 + int(a[9])*10+int(a[10])

    sum = sum + end - start
print(sum)

"""
10:00 19:00
09:00 15:00
10:00 11:00
11:00 22:00
09:00 15:00
"""