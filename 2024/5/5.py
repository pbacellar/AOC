from functools import partial
from collections import defaultdict

with open("input.txt", "r") as f:
    lines = f.read().split("\n")

rules = defaultdict(lambda: defaultdict(list))
for rule in map(partial(str.split, sep="|"), lines[: lines.index("")]):
    rules[rule[0]]["after"].append(rule[1])
    rules[rule[1]]["before"].append(rule[0])

updates = list(map(partial(str.split, sep=","), lines[lines.index("") + 1 :]))

# print(rules)
# print(updates)

mid_sum = 0
for update in updates:
    ok = True
    for idx, u in enumerate(update):
        if any(x in rules[u]["after"] for x in update[:idx]):
            ok = False
            break
    if ok:
        # print(update[len(update)//2])
        mid_sum += int(update[len(update) // 2])
print(mid_sum)

# Part 2
incorrect_updates = []
for update in updates:
    for idx, u in enumerate(update):
        if any(x in rules[u]["after"] for x in update[:idx]):
            incorrect_updates.append(update)
            break



def do(rules, update):
    swapped = False
    for idx, u in enumerate(update):
        for idx_x, x in enumerate(update[:idx]):
            # print(idx, u, idx_x, x, end = " ")
            if x in rules[u]["after"]:
                # print("swap")
                update[idx] = x
                update[idx_x] = u
                # print(update)
                swapped = True
                break
            # else:
                # print("")
    return swapped


mid_sum = 0
for update in incorrect_updates:
    # print(update)
    swapped = True
    while swapped:
        swapped = do(rules, update)
    mid_sum += int(update[len(update) // 2])
    # print(update)

print(mid_sum)
