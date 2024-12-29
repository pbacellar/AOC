from collections import defaultdict
from functools import reduce, cache

with open("input.txt", "r") as f:
    stones = [int(stone) for stone in f.read().split()]


class Node:
    def __init__(self, value, next=None, times_to_blink=0, parent=None):
        self.value = value
        self.next = next
        self.times_to_blink = times_to_blink
        self.visited = False
        self.parent = parent


node = Node(stones[len(stones)-1], None)
for idx in range(len(stones) - 2, -1, -1):
    node = Node(stones[idx], node)

# while node:
#     print(node.value)
#     node = node.next


def blink(node: Node):
    node_count = 0
    while node:
        node_count += 1
        if node.value == 0:
            node.value = 1
        elif len(str(node.value)) % 2 == 0:
            # print(node.value)
            new_node = Node(int(str(node.value)[len(str(node.value)) // 2:]), node.next)
            node.value = int(str(node.value)[:len(str(node.value)) // 2])
            node.next = new_node
            # print(node.value)
            # print(new_node.value)
            # print()
            node = new_node
            node_count += 1
        else:
            node.value *= 2024
        node = node.next
    return node_count


for i in range(25):
    # print(i)
    temp_node = node
    # while temp_node:
    #     print(temp_node.value, end = " ")
    #     temp_node = temp_node.next
    # print()
    count = blink(node)
print("part1", count)

# Part 2 try 1
# with open("input.txt", "r") as f:
#     stones = [int(stone) for stone in f.read().split()]

# times_to_blink = 75
# node = Node(stones[len(stones)-1], None, times_to_blink=times_to_blink)
# for idx in range(len(stones) - 2, -1, -1):
#     node = Node(stones[idx], node, times_to_blink=times_to_blink)


# def blink_n_times(node: Node, n_blinks, cache = None):
#     cache = cache or dict()
#     node_count = 0
#     while node:
#         old_value = node.value
#         # print("before", node.value, node.times_to_blink, end = " ")
#         node_count += 1 if not node.visited else 0
#         node.visited = True

#         if node.times_to_blink <= 0:
#             node = node.next
#             # print("next")
#             continue

#         node.times_to_blink -= 1
#         if old_value in cache:
#             if cache[node.value][1]:
#                 new_node = Node(cache[node.value][1], node.next, node.times_to_blink)
#                 node.value = cache[node.value][0]
#                 node.next = new_node
#             else:
#                 node.value = cache[node.value][0]
#         elif node.value == 0:
#             node.value = 1
#             cache[old_value] = (node.value, None)
#         elif len(str(node.value)) % 2 == 0:
#             # print(node.value)
#             new_node = Node(int(str(node.value)[len(str(node.value)) // 2:]), node.next, node.times_to_blink)
#             node.value = int(str(node.value)[:len(str(node.value)) // 2])
#             node.next = new_node
#             cache[old_value] = (node.value, new_node.value)
#         else:
#             node.value *= 2024
#             cache[old_value] = (node.value, None)
#         # print("after", node.value, "node.next", node.next.value, node.next.times_to_blink)
#     return node_count

# print("Start")
# count = blink_n_times(node, times_to_blink)
# print(count)

# part 2 try 2
with open("input.txt", "r") as f:
    stones = [int(stone) for stone in f.read().split()]


def cacher(func):
    cache_ = dict()

    def wrapper(*args):
        if args not in cache_:
            cache_[args] = func(*args)
        return cache_[args]
    
    return wrapper

cache_ = dict()
# @cacher
def blink_n_times(stone, n_times):
    global cache_
    count = 0
    if cache_.get((stone, n_times)):
        return cache_[(stone, n_times)]
    if n_times <= 0:
        return 1
    if stone == 0:
        count = blink_n_times(1, n_times-1)
        cache_[(1, n_times-1)] = count
    elif len(str(stone)) % 2 == 0:
        count1 = blink_n_times(int(str(stone)[:len(str(stone)) // 2]), n_times-1)
        count2 = blink_n_times(int(str(stone)[len(str(stone)) // 2:]), n_times-1)
        count += count1 + count2
        cache_[(int(str(stone)[:len(str(stone)) // 2]), n_times-1)] = count1
        cache_[(int(str(stone)[len(str(stone)) // 2:]), n_times-1)] = count2
        cache_[(stone, n_times)] = count
    else:
        count += blink_n_times(stone * 2024, n_times-1)
        cache_[(stone * 2024, n_times-1)] = count
    return count


n_times = 75
res = sum(blink_n_times(x, n_times) for x in stones)
print("part2", res)
# 0
# 1
# 2024
# 20 24
# 2 0 2 4
# 4048 1 4048 8096
# 40 48 2024 40 48 80 96
# 4 0 4 8 20 24 4 0 4 8 8 0 9 6