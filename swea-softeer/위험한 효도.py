a, b, d = map(int, input().split())
dis = d
time = 0

while dis > a:
    dis -= a
    time += a
    time += b

time += dis
dis = d

while dis > b:
    dis -= b
    time += b
    time += a
time += dis

print(time)