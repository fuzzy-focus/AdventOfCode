print(f"Day {__file__[:-3]}")
with open("03.txt") as f:
    data = f.read().splitlines()

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
trees = {(sx,sy): [data[i*sy][i*sx % len(data[0])] for i in range(len(data)//sy)].count('#') for sx, sy in slopes}
print(f"Part 1: {trees[(3,1)]}")
prod=1
for t in trees.values():
    prod *= t
print(f"Part 2: {prod}")

