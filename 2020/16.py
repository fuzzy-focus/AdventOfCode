import itertools
import collections
import re

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

example1 = """\
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".strip()

example2 = """\
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".strip()

get_ints = lambda text: [int(x) for x in re.findall(r"\d+", text)]

def get_rule(line):
    rule, numbers = line.split(":")
    lb1, ub1, lb2, ub2 = get_ints(numbers)
    cond = lambda x: lb1<=x<=ub1 or lb2<=x<=ub2
    return rule, cond

def parse_input(text):
    rtext, ttext, nttext = text.split('\n\n')
    rules = dict(map(get_rule, rtext.splitlines()))
    my_ticket = get_ints(ttext)
    tickets = [get_ints(t) for t in nttext.splitlines()[1:]]
    return rules, my_ticket, tickets

# Part 1

#text = example1
rules, my_ticket, tickets = parse_input(text)

inv_tickets = [[val for val in ticket if not any(rule(val) for rule in rules.values())] for ticket in tickets]
result =  sum(sum(inv_tickets, []))
print(f"Part 1: {result}")

# Part 2

#text = example2
#rules, my_ticket, tickets = parse_input(text)

val_tickets = [ticket for ticket in tickets if all(any(rule(val) for rule in rules.values()) for val in ticket)]
val_rules = [
    set(
        rule
        for rule, cond in rules.items()
        if all(cond(val) for val in col)
    )
    for col in zip(*val_tickets)
]

rule_mapping = {}
unresolved_rules = dict(enumerate(val_rules))
result = 1
while unresolved_rules:
    i = min(unresolved_rules, key=lambda x:len(unresolved_rules[x]))
    rules = unresolved_rules.pop(i)
    if len(rules) != 1:
        raise Exception("should not happen")
    unresolved_rules = {i:r-rules for i,r in unresolved_rules.items()}
    rule = rules.pop()
    rule_mapping[rule] = i
    if rule.startswith("departure"):
        result *= my_ticket[i]

print(f"Part 2: {result}")
