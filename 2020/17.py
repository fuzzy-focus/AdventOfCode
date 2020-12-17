import itertools
import collections

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

plane = [[cube == "#" for cube in line] for line in text.split()]

cube_3d = collections.namedtuple("cube", "x y z", defaults=[0,0,0])

class Grid:

    def __init__(self, plane, neighbour_fun, alive_fun, coord_type=cube_3d):
        self.grid = {coord_type(x,y) for y, row in enumerate(plane) for x, cube in enumerate(row)  if cube}
        self.alive = alive_fun
        self.neighbours = neighbour_fun

    def step(self):
        act_neighbours = collections.defaultdict(int)
        for cube in self.grid:
            for n in self.neighbours(cube):
                act_neighbours[n] += 1
        self.grid = {cube for cube, n in act_neighbours.items() if self.alive(cube in self.grid, n)}

    def __len__(self):
        return len(self.grid)

# Part 1

def neighbours(point, dim=3):
    return {tuple(a+b for a,b in zip(point, delta)) for delta in itertools.product([-1,0,1],repeat=dim) if any(delta)}

def alive(active, neighbours):
    if active:
        return neighbours == 2 or neighbours == 3
    else:
        return neighbours == 3

grid = Grid(plane, neighbour_fun=neighbours, alive_fun=alive)

for i in range(6):
    grid.step()

print(f"Part 1: {len(grid)}")

# Part 2

cube_4d = collections.namedtuple("cube", "x1 x2 x3 x4", defaults=[0,0,0,0])
n2 = lambda p: neighbours(p, dim=4)
grid = Grid(plane, neighbour_fun=n2, alive_fun=alive, coord_type=cube_4d)

for i in range(6):
    grid.step()

print(f"Part 2: {len(grid)}")

