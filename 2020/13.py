import itertools

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

t,busses = text.split()
t = int(t)
busses_i = [(int(b),i) for i, b in enumerate(busses.split(',')) if b != "x"]
busses = [b for b, _ in busses_i]

tp_busses = [b*(t//b if t%b == 0 else 1+t//b)-t for b in busses]
print(tp_busses)
min_time = min(tp_busses)
bid = busses[tp_busses.index(min_time)]
print(f"Part 1: {bid * min_time}")
print(sorted(busses_i))
#for i in itertools.count(100000000000000//busses_i[0][0]):
#    t = busses_i[0][0] * i
#    land_correct = [(t+i)%b==0 for b,i in busses_i[1:]]
#    if all(land_correct):
#        break
#print(f"Part 2: {t}")

