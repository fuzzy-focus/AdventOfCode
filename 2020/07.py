import re
import collections
from pprint import pprint

with open("07.txt") as f:
    text = f.read()

rule_pattern = re.compile(r"(.*) bags contain (.*)\.")
bag_pattern = re.compile(r"(\d+) (.+?) bag")
rules = rule_pattern.findall(text)
rd = {}
rrd = collections.defaultdict(list)
for bag, bags in rules:
    if "no other bags" in bags:
        rd[bag] = {}
    else:
        dbags = bag_pattern.findall(bags)
        rd[bag] = {col: int(num) for num, col in dbags}
        for _, col in dbags:
            rrd[col].append(bag)
visited = set()
to_visit = collections.deque(["shiny gold"])

while to_visit:
    bag = to_visit.popleft()
    visited.add(bag)
    for ob in rrd[bag]:
        if ob not in visited:
            to_visit.append(ob)
print(f"Part 1: {len(visited)-1}")

def recursive_bags(bag):
    if not rd[bag]:
        result = 1
    else:
        result = 1 + sum([i*recursive_bags(b) for b, i in rd[bag].items()])
    #print(f"{bag} contains {result} bags")
    return result

#pprint(rd)
print(f"Part 2: {recursive_bags('shiny gold')-1}")
