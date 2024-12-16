from itertools import product

with open("input.txt", "r") as f:
    # lines = f.read().splitlines()
    lines = [
        [[int(line.split(":")[0])]] + [list(map(int, line.split(":")[1].split()))]
        for line in f.read().splitlines()
    ]
# print(lines)
ops = ["*", "+"]
sum_ = 0
for idx, line in enumerate(lines):
    target = line[0][0]
    # print(target, line[1])
    perms = list(product(ops, repeat=len(line[1]) - 1))
    # print(perms)
    for perm in perms:
        cum = 0
        curr = line[1][0]
        for op, num in zip(perm, line[1][1:]):
            # print(curr, op, num, end=" = ")
            if op == "+":
                curr += num
            else:
                curr *= num
            # print(curr)
        if curr == target:
            # print("HIT")
            sum_ += target
            break
print(sum_)

# Part 2


def concat_op(num1, num2):
    return int(str(num1) + str(num2))


ops = ["*", "+", "||"]
sum_ = 0
for idx, line in enumerate(lines):
    target = line[0][0]
    # print(target, line[1])
    perms = list(product(ops, repeat=len(line[1]) - 1))
    # print(perms)
    for perm in perms:
        cum = 0
        curr = line[1][0]
        for op, num in zip(perm, line[1][1:]):
            # print(curr, op, num, end=" = ")
            if op == "+":
                curr += num
            elif op == "*":
                curr *= num
            elif op == "||":
                curr = concat_op(curr, num)
            # print(curr)
        if curr == target:
            # print("HIT")
            sum_ += target
            break
print(sum_)
