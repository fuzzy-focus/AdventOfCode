import re

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

passports = text.split('\n\n')
fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid",}
fields.discard("cid")

data = [re.findall(r"(\S+):(\S+)", pp) for pp in passports]
data = [{a:b for a,b in pp} for pp in data]
valid = [set(pp.keys()) for pp in  data if set(pp.keys()).issuperset(fields)]
print(f"part 1: {len(valid)}")


"""
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
"""

def condition(d):
    byr = 1920 <= int(d.get("byr",0)) <= 2002
    iyr = 2010 <= int(d.get("iyr",0)) <= 2020
    eyr = 2020 <= int(d.get("eyr",0)) <= 2030
    hcl = bool(re.match(r"#[0-9a-fA-F]{6}", d.get("hcl","")))
    ecl = d.get("ecl","nope") in ("amb blu brn gry grn hzl oth")
    pid = d.get("pid","")
    pid = pid.isdigit() and len(pid) == 9
    hgt = d.get("hgt", "")
    m = re.findall(r"(\d+)(in|cm)", hgt)
    if m:
        hgt, unit = m[0]
        if unit == "cm":
            hgt = 150 <= int(hgt) <= 193
        elif unit == "in":
            hgt = 59 <= int(hgt) <= 76
        else:
            hgt = False
    else:
        hgt = False
    cond = [byr, iyr, eyr, hcl, ecl, pid, hgt]
    return all(cond)

valid2 = [pp for pp in data if condition(pp)]

print(f"part 2: {len(valid2)}")
