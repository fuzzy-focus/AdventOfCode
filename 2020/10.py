from pprint import pprint

with open("10.txt") as f:
    text = f.read()

ad = [int(i) for i in text.split()]
ad.append(0)
ad.append(max(ad)+3)
ad = sorted(ad)
d = [b-a for a,b in zip(ad[:-1], ad[1:])]
print(f"Part 1: {d.count(1)*d.count(3)}")
#{adapter: [adapters that can come before that adapter}
nm = {a: [n for n in ad[max(i-4, 0):i] if a-3 <= n] for i, a in enumerate(ad)} 
#number of paths from a given adapter to the end
paths = {ad[-1]:1}

for a in reversed(ad):
    for prev in nm[a]:
        paths[prev] = paths.get(prev,0) + paths[a]

print(f"Part 2: {paths[0]}")
