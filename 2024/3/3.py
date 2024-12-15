import re
from functools import reduce

with open("input.txt", "r") as f:
    text = f.read()

print(sum(reduce(int.__mul__, map(int, find)) for find in re.findall(r"mul\((\d+),(\d+)\)", text)))


# Part 2
def do_mul(mul_op):
    return reduce(int.__mul__, (map(int, mul_op[4:-1].split(","))))


finds = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", text)

active = True
mul_sum = 0
for find in finds:
    if find == "do()":
        active = True
    elif find == "don't()":
        active = False
    elif active:
        mul_sum += do_mul(find)

print(mul_sum)
