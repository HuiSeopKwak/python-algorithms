max_people = 0
state = 0

for i in range(4):
    outV, inV = map(int, input().split())
    state -= outV
    state += inV
    if max_people < state:
        max_people = state
print(max_people)