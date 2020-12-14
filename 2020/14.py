import re
import itertools

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

mask_pat = re.compile(r"mask = ([01X]+)")
mem_pat = re.compile(r"mem\[(\d+)\] = (\d+)")

# part 1
mask = None
mem = {}

def mask_fun(bm):
    m1 = int(bm.replace('X','0'),base=2)
    m0 = int(bm.replace('X','1'), base=2)
    return lambda x: (x|m1) & m0

for line in text.split('\n'):
    mask_match = mask_pat.match(line)
    if mask_match:
        mask = mask_fun(mask_match.group(1))
        continue
    mem_match = mem_pat.match(line)
    if mem_match:
        addr, val = mem_match.groups()
        mem[int(addr)] = mask(int(val))

print(f"Part 1: {sum(mem.values())}")

# part 2
mask = None
mem = {}

def mask_fun(bm):
    n = bm.count('X')
    pos = [i for i,d in enumerate(bm) if d == 'X']
    def masks(addr):
        if n == 0:
            return [int(bm,base=2)]
        addr = f"{addr:0>36b}"
        addr = ''.join('1' if m == '1' else a for a,m in zip(addr, bm))
        for rep in itertools.product("01", repeat=n):
            mask = list(addr)
            for p, r in zip(pos,rep):
                mask[p] = r
            yield int(''.join(mask),base=2)
    return masks

for line in text.split('\n'):
    mask_match = mask_pat.match(line)
    if mask_match:
        mask = mask_fun(mask_match.group(1))
        continue
    mem_match = mem_pat.match(line)
    if mem_match:
        addr, val = mem_match.groups()
        for ad in mask(int(addr)):
            mem[ad] = int(val)

print(f"Part 2: {sum(mem.values())}")
