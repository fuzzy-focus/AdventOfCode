import itertools
import collections

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

numbers = [int(x) for x in text.strip().split(',')]

turn = itertools.count(1)
d = collections.defaultdict(lambda: collections.deque(maxlen=2))
for n, t in zip(numbers, turn):
    d[n].append(t)

def do_turn(d,t,n):
    p = d[n]
    if len(p) == 2:
        n = p[1]-p[0]
    else:
        n = 0
    d[n].append(t)
    return d,n


# Part 1

for t in turn:
    d,n = do_turn(d,t,n)
    if t == 2020:
        break

print(f"Part 1: {n}")

# Part 2

for t in turn:
    d,n = do_turn(d,t,n)
    if t == 30000000:
        break

print(f"Part 2: {n}")
