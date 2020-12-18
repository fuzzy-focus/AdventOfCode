import re

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

lines = text.replace(" ","").splitlines()

inner_pattern = re.compile(r"\([0-9+*]+\)")
expr_pattern = re.compile(r"([0-9]+|[*]|[+])")

def eval_line(line):
    while "(" in line:
        for m in inner_pattern.findall(line):
            line = line.replace(m, eval_expr(m))
    return int(eval_expr(line))


# EVAL-BASED ATROCITIES UP AHEAD! READ AT YOUR OWN RISK!

# Part 1

def eval_expr(expr):
    comp = expr_pattern.findall(expr)
    result = int(comp[0])
    for op, num in zip(comp[1::2],comp[2::2]):
        result = eval(str(result) + op + num)
    return str(result)

p1 = sum(eval_line(line) for line in lines)

print(f"Part 1: {p1}")

# Part 2:

expr_pattern = re.compile(r"(\d+(?:\+\d+)*|[*])")

def eval_expr(expr):
    comp = expr_pattern.findall(expr)
    result = eval(comp[0])
    for op, num in zip(comp[1::2],comp[2::2]):
        result = eval(str(result) + op + str(eval(num)))
    return str(result)

p2 = sum(eval_line(line) for line in lines)

print(f"Part 2: {p2}")
