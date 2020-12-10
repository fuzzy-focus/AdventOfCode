print(f"Day {__file__[:-3]}")
#5-11 t: glhbttzvzttkdx
#2-4 f: cfkmf
#9-12 m: mmmmmmmmmmmmm
#2-10 z: vghqbzbcxf
import re

with open("02.txt") as f:
    data = re.findall(r"(\d+)-(\d+) (\w): (\w+)", f.read())

data = [(int(a), int(b), c, d) for a,b,c,d in data]

p1 = len([(a,b,c,d) for a,b,c,d in data if a <= d.count(c) <= b])
print(f"Part 1: {p1}")


p2= len([(a,b,c,d) for a,b,c,d in data if (d[a-1] == c) != (d[b-1] == c)])
print(f"Part 2: {p2}")
