from pprint import pprint

day = __file__[:-3]
print(f"Day {day}")
with open(f"{day}.txt") as f:
    text = f.read()

allergs = {}
ingredient_list = []
allergen_list = []
all_ingredients = set()
all_allergens = set()

for line in text.strip().splitlines():
    ingredients, allergens = line.split("(")
    ingredients = ingredients.strip().split()
    allergens = allergens[9:-1].strip().split(", ")
    all_ingredients |= set(ingredients)
    all_allergens |= set(allergens)
    for alg in allergens:
        if alg in allergs:
            allergs[alg] &= set(ingredients)
        else:
            allergs[alg] = set(ingredients)
    ingredient_list.append(ingredients)
    allergen_list.append(allergens)


ingr_candidates = set()
for ingrs in allergs.values():
    ingr_candidates |= ingrs
allergen_free = all_ingredients - ingr_candidates

# Part 1

tally = sum(sum(1 for ingr in allergen_free if ingr in food_ingrs) for food_ingrs in ingredient_list)

print(f"Part 1: {tally}")

# Part 2

unresolved_allergens = set(all_allergens)
resolved_allergens = {}
while unresolved_allergens:
    allerg = min(allergs, key=lambda x:len(allergs[x]))
    ingr = allergs.pop(allerg)
    if len(ingr) != 1:
        raise Exception("Something went wrong!")
    else:
        ingr = ingr.pop()
    resolved_allergens[allerg] = ingr
    unresolved_allergens.remove(allerg)
    for alg in allergs:
        allergs[alg] -= set((ingr,))

dangerous_ingr = [ingr for _, ingr in sorted(resolved_allergens.items())]
r = ','.join(dangerous_ingr)
print(f"Part 2: {r}")


