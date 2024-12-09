li = {
    '0' : '1110111', #0
    '1' : '0010010', #1
    '2' : '1011101', #2
    '3' : '1011011', #3
    '4' : '0111010', #4
    '5' : '1101011', #5
    '6' : '1101111', #6
    '7' : '1110010', #7
    '8' : '1111111', #8
    '9' : '1111011', #9
    ' ' : '0000000' #nothing
}
T = int(input())
for _ in range(T):
    a, b = map(str, input().split())
    a_zero = 5 - len(a)
    b_zero = 5 - len(b)
    a = ' '*a_zero + a
    b = ' '*b_zero + b

    result = 0
    for i in range(5):
        for j in range(7):
            if li[a[i]][j] != li[b[i]][j]:
                result += 1

    print(result)