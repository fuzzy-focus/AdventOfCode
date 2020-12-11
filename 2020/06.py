import functools
import operator
from pprint import pprint

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

forms = [g.strip().split("\n") for g in text.split("\n\n")]

counts = [len(functools.reduce(operator.or_,map(set,group))) for group in forms]
print(f"Part 1: {sum(counts)}")
counts = [len(functools.reduce(operator.and_,map(set,group))) for group in forms]
print(f"Part 2: {sum(counts)}")
