import re

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

example = """\
0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""
#text = example

rule_text, messages = text.split("\n\n")
messages = messages.splitlines()

def get_rules_dict():
    rules = {}
    for line in rule_text.splitlines():
        ind, *elements = line.split(" ")
        rule_index = ind[:-1] # remove ':'
        if len(elements) == 1 and '"' in elements[0]:
            rules['r'+rule_index] = elements[0].strip('"')
        else:
            rule = '({r' + '}{r'.join(elements) + '})'
            rule = rule.replace('{r|}','|')
            rules['r'+rule_index] = rule
    return rules


# Part 1
rules = get_rules_dict()
changes = True
while changes:
    changes = False
    for ind, rule in rules.items():
        new_rule = rule.format(**rules)
        changes = changes or (new_rule != rule)
        rules[ind] = new_rule

p1 = [msg for msg in messages if re.match('^'+rules["r0"]+'$', msg)]
print(f"Part 1: {len(p1)}")

# Part 2:
rules = get_rules_dict()

# hand-fudge the recursive rules
rules["r8"] = "({r42})+"
rules["r11"] = '(' + '|'.join("(" + "{r42}"*i + "{r31}"*i +")" for i in range(1,35)) + ')'

changes = True
while changes:
    changes = False
    for ind, rule in rules.items():
        new_rule = rule.format(**rules)
        changes = changes or (new_rule != rule)
        rules[ind] = new_rule

print(rules["r0"])
p2 = [msg for msg in messages if re.match('^'+rules["r0"]+'$', msg)]
print(f"Part 2: {len(p2)}")
