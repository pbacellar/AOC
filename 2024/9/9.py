from itertools import zip_longest

with open("input.txt", "r") as f:
    l = f.read()

l2 = []
for i, (c1, c2) in enumerate(zip_longest(l[::2], l[1::2])):
    l2.extend([str(i)] * int(c1))
    l2.extend(["."] * int(c2) if c2 else [])

print(l2)
print("".join(l2))
# print("".join(l[::2]))
# print("".join(l[1::2]))


def get_next_block(l):
    for idx, c in enumerate(l[::-1]):
        if c != ".":
            yield ((len(l) - idx - 1), c)


next_block_iter = get_next_block(l2)
stop = False
checksum = 0
for idx1, c1 in enumerate(l2):
    # print(idx1, c1, end="    ")
    if c1 != ".":
        # checksum += int(l2[idx1]) * idx1
        continue
    try:
        idx2, c2 = next(next_block_iter)
        if idx2 <= idx1:
            break
    except StopIteration:
        # print("".join(l2))
        break
    l2[idx2] = "."
    l2[idx1] = c2
    # checksum += int(l2[idx1]) * idx1
    # print("".join(l2))


for idx in range(0, len(l2)):
    if l2[idx] == ".":
        break
    checksum += int(l2[idx]) * idx

# print("".join(l2))
print(checksum)

# Part 2


def safe_get_item(l, idx):
    try:
        return l[idx]
    except IndexError:
        return None


def from itertools import zip_longest

with open("input.txt", "r") as f:
    l = f.read()

l2 = []
for i, (c1, c2) in enumerate(zip_longest(l[::2], l[1::2])):
    l2.extend([str(i)] * int(c1))
    l2.extend(["."] * int(c2) if c2 else [])


def get_next_block_idx_backwards(l, idx_offset=0):
    for idx, c in enumerate(l[len(l)-1-idx_offset::-1]):
        if c != ".":
            yield len(l) - idx - 1


def safe_iter(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None


next_block_iter = get_next_block_idx_backwards(l2)
stop = False
checksum = 0
for idx1, c1 in enumerate(l2):
    if c1 != ".":
        continue
    idx2 = safe_iter(next_block_iter)
    if not idx2:
        break
    c2 = l2[idx2]
    if idx2 <= idx1:
        break
    l2[idx2] = "."
    l2[idx1] = c2

for idx in range(0, len(l2)):
    if l2[idx] == ".":
        break
    checksum += int(l2[idx]) * idx

print(checksum)

# Part 2
l2 = []
for i, (c1, c2) in enumerate(zip_longest(l[::2], l[1::2])):
    l2.extend([str(i)] * int(c1))
    l2.extend(["."] * int(c2) if c2 else [])

next_block_iter = get_next_block_idx_backwards(l2)
# read next id block - get first and last ids
while (idx_last_block := safe_iter(next_block_iter)) is not None:
    if not idx_last_block:
        break
    for idx_first_block in range(len(l2) - (len(l2) - idx_last_block), -1, -1):
        if l2[idx_first_block] != l2[idx_last_block]:
            break
    idx_first_block = idx_first_block if idx_first_block == 0 else idx_first_block + 1
    for _ in range(idx_first_block, idx_last_block):
        safe_iter(next_block_iter)

    for idx1 in range(len(l2[0:idx_first_block])):
        if l2[idx1] != ".":
            continue

        for idx_last_dot in range(idx1, len(l2)):
            if l2[idx_last_dot] != ".":
                break
        idx_last_dot = idx_last_dot if idx_last_dot == len(l2) - 1 else idx_last_dot - 1
        if (idx_last_dot - idx1) < (idx_last_block - idx_first_block):
            continue
        else:
            dot_offset = (idx_last_block - idx_first_block)
            temp = l2[idx1:idx1+dot_offset+1]
            l2[idx1:idx1+dot_offset+1] = l2[idx_first_block:idx_last_block+1]
            l2[idx_first_block:idx_last_block+1] = temp
            break

checksum = 0
for idx in range(0, len(l2)):
    if l2[idx] == ".":
        continue
    checksum += int(l2[idx]) * idx
# print("".join(l2))
print(checksum)
get_next_block2(l=[], peek=False, peek_offset=1):
    if not getattr(get_next_block2, "idx", None):
        get_next_block2.idx = 0
    if peek:
        r = safe_get_item(l, get_next_block2.idx + peek_offset)
        if r:
            return r, get_next_block2.idx + peek_offset
        else:
            return None, None
    else:
        r = safe_get_item(l, get_next_block2.idx)
        if r:
            get_next_block2.idx += 1
            return r, get_next_block2.idx
        else:
            return None, None


def get_next_block3(l=[], peek=False, peek_offset=1):
    if not getattr(get_next_block3, "idx", None):
        get_next_block3.idx = 0
    if peek:
        r = safe_get_item(l, get_next_block3.idx + peek_offset)
        if r:
            return r, len(l) - (get_next_block3.idx + peek_offset)
        else:
            return None, None
    else:
        r = safe_get_item(l, get_next_block3.idx)
        if r:
            get_next_block3.idx += 1
            return r, len(l) - get_next_block3.idx
        else:
            return None, None


def peek_blocks(l):
    q, idx0 = get_next_block2(l, peek=True, peek_offset=0)
    idx_start_blocks = idx0
    peek_offset = 1
    r, idx1 = get_next_block2(l, peek=True, peek_offset=peek_offset)
    # print(q, r, idx0, idx1)
    while q == r and (q is not None or r is not None):
        q = r
        idx0 = idx1
        peek_offset += 1
        r, idx1 = get_next_block2(l, peek=True, peek_offset=peek_offset)
        # print(q, r, idx0, idx1)
    idx_end_blocks = idx0
    return idx_start_blocks, idx_end_blocks


def peek_blocks2(l):
    q, idx0 = get_next_block3(l, peek=True, peek_offset=0)
    idx_end_blocks = idx0
    peek_offset = 1
    r, idx1 = get_next_block3(l, peek=True, peek_offset=peek_offset)
    # print(q, r, idx0, idx1)
    while q == r and (q is not None or r is not None):
        q = r
        idx0 = idx1
        peek_offset += 1
        r, idx1 = get_next_block3(l, peek=True, peek_offset=peek_offset)
        # print(q, r, idx0, idx1)
    idx_start_blocks = idx0
    return idx_start_blocks, idx_end_blocks


l2 = []
for i, (c1, c2) in enumerate(zip_longest(l[::2], l[1::2])):
    l2.extend([str(i)] * int(c1))
    l2.extend(["."] * int(c2) if c2 else [])

stop = False
checksum = 0
idx1_offset = 0

for idx1, c1 in enumerate(l2):
    new_idx1 = idx1 + idx1_offset
    if new_idx1 >= len(l2):
        break
    # print(idx1, c1, end="    ")
    if c1 != ".":
        get_next_block2(l2)
        # checksum += int(l2[idx1]) * idx1
        continue

    idx_start_blocks_dots, idx_end_blocks_dots = peek_blocks(l2)
    idx_start_blocks, idx_end_blocks = peek_blocks2(l2[::-1])
    print(idx_start_blocks_dots, idx_end_blocks_dots)
    print(idx_start_blocks, idx_end_blocks)

    if (idx_end_blocks_dots - idx_start_blocks_dots) < (idx_end_blocks - idx_start_blocks):
        print("cant move")
        idx1_offset += (idx_end_blocks_dots - idx_start_blocks_dots)
        continue
    else:

    break
    idx2, c2 = idx1, r
    l2[idx2] = "."
    l2[new_idx1] = c2
    # checksum += int(l2[idx1]) * idx1
    # print("".join(l2))


for idx in range(0, len(l2)):
    if l2[idx] == ".":
        break
    checksum += int(l2[idx]) * idx

print(checksum)
