import itertools

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

stream = [int(i) for i in text.split()]
N=25
for i in range(len(stream)-N-1):
    if stream[i+N] not in [a+b for a,b in itertools.combinations(stream[i:i+N],2)]:
        break
result = stream[i+N]
print(f"Part 1: {result}")

stream = stream[::-1]
for i in range(len(stream)):
    for j in range(2,len(stream)-i):
        s = sum(stream[i:i+j])
        if s >= result:
            break
    if s == result:
        result = max(stream[i:i+j]) + min(stream[i:i+j])
        break
print(f"Part 2: {result}")

