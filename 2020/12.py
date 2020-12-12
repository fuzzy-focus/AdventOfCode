from pprint import pprint
import itertools

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()
example = """\
F10
N3
F7
R90
F11"""

#text = example

dirs = [(d[0], int(d[1:])) for d in text.split()]

# part 1

move = {
    "L": lambda p, h, n: (p, h*(1j)**(n//90)),
    "R": lambda p, h, n: (p, h*(-1j)**(n//90)),
    "F": lambda p, h, n: (p + n*h, h),
    "N": lambda p, h, n: (p + n*1j, h),
    "S": lambda p, h, n: (p - n*1j, h),
    "E": lambda p, h, n: (p + n, h),
    "W": lambda p, h, n: (p - n, h),
}

p, h = 0, 1
for c, n in dirs:
    p,h = move[c](p,h,n)

print(f"Part 1: {abs(p.real) + abs(p.imag)}")

# part 2

move = {
    "L": lambda p, h, n: (p, h*(1j)**(n//90)),
    "R": lambda p, h, n: (p, h*(-1j)**(n//90)),
    "F": lambda p, h, n: (p + n*h, h),
    "N": lambda p, h, n: (p, h + n*1j),
    "S": lambda p, h, n: (p, h - n*1j),
    "E": lambda p, h, n: (p, h + n),
    "W": lambda p, h, n: (p, h - n),
}

p, h = 0, 10+1j
for c, n in dirs:
    p,h = move[c](p,h,n)

print(f"Part 1: {abs(p.real) + abs(p.imag)}")
