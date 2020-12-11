from pprint import pprint
import itertools

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()


class SeatingArea:

    def __init__(self, area, neighbour_fun, threshold=4):
        self.seats = {(x,y) for y, row in enumerate(area) for x, seat in enumerate(row)  if seat != "."}
        self.threshold = threshold
        self.neighbours = neighbour_fun


    def seat_step(self, seat, occupied):
        x,y = seat
        occ = seat in occupied
        ocn = len(self.neighbours(*seat, self.seats) & occupied)
        if not occ and ocn == 0:
            return True
        elif occ and ocn >= self.threshold:
            return False
        else:
            return occ

    def step(self, occupied):
        new_occ =  {seat for seat in self.seats if self.seat_step(seat, occupied)}
        return new_occ

    def run(self):
        occupied = set()
        for stp in itertools.count(1):
            occ_new = self.step(occupied)
            if occ_new == occupied:
                return stp, len(occ_new)
            occupied = occ_new

# Part 1

def neighbours(x,y, seats):
    return {(x+i,y+j) for i,j in itertools.product([-1,0,1],repeat=2) if i or j} & seats

area = [list(line) for line in text.split()]
seats = SeatingArea(area, neighbour_fun=neighbours)
stp, seats_taken = seats.run()

print(f"Part 1: stable after {stp} steps, {seats_taken} seats taken")

#part 2
def neighbours(x,y, seats):
    nbrs = set()
    for i,j in itertools.product([-1,0,1],repeat=2):
        if not i and not j:
            continue
        for k in itertools.count(1):
            xi, yi = (x+i*k, y+j*k)
            if not (0 <= xi < len(area[0]) and 0 <= yi < len(area)):
                break
            elif (xi,yi) in seats:
                nbrs.add((xi,yi))
                break
    return nbrs

seats = SeatingArea(area, neighbours, threshold=5)
stp, seats_taken = seats.run()

print(f"Part 2: stable after {stp} steps, {seats_taken} seats taken")


