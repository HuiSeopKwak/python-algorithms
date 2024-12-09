def check(li):
    a, b = 0, 0 # a 모음, b 자음
    for i in range(len(li)):
        if li[i] in aeiou:
            a += 1
        else:
            b += 1
    if a >= 1 and b >= 2:
        # 그냥 append(li) 하면 깊은 복사가 되어서 li 주소값을 추가하기 때문에 나중에 li의 값이 바뀌어 버리면 result 내의 값 또한 바뀌게 된다
        # 그래서 li[:]를 통해 이 당시 들어있는 li의 내부 값들을 추가해주면 나중에 li 값이 바뀌게 되어도 result 내의 값에는 변화가 없다
        result.append(li[:])

def recur(idx, cnt):
    global result, li
    if cnt == l:
        check(li)
        return
    else:
        if idx == c:
            return
        li.append(text[idx])
        recur(idx + 1, cnt + 1)
        li.pop()
        recur(idx + 1, cnt)

l, c = map(int, input().split())
text = list(input().split())
text.sort()
result, li = [], []
aeiou = ['a', 'e', 'i', 'o', 'u']

recur(0, 0)

for i in range(len(result)):
    print(''.join(result[i]))