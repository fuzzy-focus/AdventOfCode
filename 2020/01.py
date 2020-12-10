print(f"Day {__file__[:-3]}")
import itertools

with open("01.txt") as f:
    text = f.read()

data = [int(x) for x in text.split()]

p1 = [a*b for a,b in itertools.combinations(data, 2) if a+b==2020][0]
print(f"Part 1: {p1}")
p2 = [a*b*c for a,b,c in itertools.combinations(data, 3) if a+b+c==2020][0]
print(f"Part 2: {p2}")
