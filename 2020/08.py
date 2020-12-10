example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""
with open("08.txt") as f:
    text = f.read()

#text = example

instructions = [tuple([i[:3], int(i[4:])]) for i in text.strip().split("\n")]
def run_till_loop(instructions):
    visited = set()
    acc = 0
    line = 0

    while True:
        visited.add(line)
        op, num = instructions[line]
        #print(f"{line}: {op} {num} ({visited})")
        if op == "acc":
            acc += num
            line += 1
        elif op == "jmp":
            line += num
        elif op == "nop":
            line += 1
        if line in visited:
            return acc

print(f"Part 1: {run_till_loop(instructions)}")

def run(instructions):
    visited = set()
    acc = 0
    line = 0

    while True:
        visited.add(line)
        op, num = instructions[line]
        #print(f"{line}: {op} {num} ({visited})")
        if op == "acc":
            acc += num
            line += 1
        elif op == "jmp":
            line += num
        elif op == "nop":
            line += 1
        if line in visited:
            raise Exception("infinite loop")
        if line >= len(instructions):
            return acc

for i, (op, num) in enumerate(instructions):
    inst = list(instructions)
    if op == "jmp":
        inst[i] = ("nop",num)
    elif op == "nop":
        inst[i] = ("jmp", num)
    else:
        continue
    try:
        result = run(inst)
    except Exception:
        pass
    else:
        print(f"Part 2: {result}")
        break

