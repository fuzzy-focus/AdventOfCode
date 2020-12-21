import itertools

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

sections = [t.split(":") for t in text.split("\n\n")]
tiles = {int(n[5:]): list(map(list,t.split())) for n,t in sections}
borders = {}

def border_gen(tile):
    yield [tile[y][x] for x,y in zip(range(10),itertools.repeat(0))]
    yield [tile[y][x] for x,y in zip(itertools.repeat(9), range(10))]
    yield [tile[y][x] for x,y in zip(reversed(range(10)),itertools.repeat(9))]
    yield [tile[y][x] for x,y in zip(itertools.repeat(0), reversed(range(10)))]

for index, tile in tiles.items():
    borders[index] = list(border_gen(tile))

print(borders[3499])
