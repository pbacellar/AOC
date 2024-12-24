from itertools import product
from time import time

with open("input.txt", "r") as f:
    # lines = f.read().splitlines()
    lines = [
        [[int(line.split(":")[0])]] + [list(map(int, line.split(":")[1].split()))]
        for line in f.read().splitlines()
    ]


def find_idx_of_last_perm_that_stats_with_ops(perms, idx_perms_start, perm, idx_op):
    idx_search = idx_perms_start
    for idx_perm in range(idx_perms_start, len(perms[idx_perms_start:])):
        for idx_op_test, op in enumerate(perm[:idx_op + 1]):
            if perms[idx_perm][idx_op_test] != op:
                break
        idx_search = idx_perm
    return idx_search


# print(lines)
ops = ["*", "+"]
sum_ = 0
start_t = time()
for idx, line in enumerate(lines):
    target = line[0][0]
    # print(target, line[1])
    perms = list(product(ops, repeat=len(line[1]) - 1))
    idx_perm_offset = 0
    for idx_perm in range(len(perms)):
        idx_perm = idx_perm + idx_perm_offset
        print(idx_perm)
        cum = 0
        curr = line[1][0]
        for idx_op, (op, num) in enumerate(zip(perms[idx_perm], line[1][1:])):
            print(idx_op, curr, op, num, end=" = ")
            if op == "+":
                curr += num
                if curr > target:
                    idx_perm_offset = find_idx_of_last_perm_that_stats_with_ops(perms, idx_perm, perms[idx_perm], idx_op)
                    break
            else:
                curr *= num
            print(curr)
        if curr == target:
            print("HIT")
            sum_ += target
            break
print(sum_)
print(time() - start_t)

# Part 2


def concat_op(num1, num2):
    return int(str(num1) + str(num2))


# ops = ["*", "+", "||"]
# sum_ = 0
# for idx, line in enumerate(lines):
#     target = line[0][0]
#     # print(target, line[1])
#     perms = product(ops, repeat=len(line[1]) - 1)
#     # print(perms)
#     for perm in perms:
#         cum = 0
#         curr = line[1][0]
#         for op, num in zip(perm, line[1][1:]):
#             # print(curr, op, num, end=" = ")
#             if op == "+":
#                 curr += num
#             elif op == "*":
#                 curr *= num
#             elif op == "||":
#                 curr = concat_op(curr, num)
#             # print(curr)
#         if curr == target:
#             # print("HIT")
#             sum_ += target
#             break
# print(sum_)
