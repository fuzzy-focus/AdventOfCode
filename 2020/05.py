with open("05.txt") as f:
    data = f.read().splitlines()

s2id = lambda x: int(x.replace("B","1").replace("F","0").replace("L","0").replace("R","1"), base=2)

nums = [s2id(d) for d in data]
print(f"Part 1: {max(nums)}")

n2 = sorted(nums)
print(f"Part 2: {[a+1 for a,b in zip(n2[:-1],n2[1:]) if b-a>1][0]}")
