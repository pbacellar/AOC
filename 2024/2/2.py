with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [list(map(int, line)) for line in map(str.split, lines)]
print(lines[:2])

xxx = [list() for _ in range(len(lines))]

for idx, line in enumerate(lines):
    for i1, i2 in zip(line[:-1], line[1:]):
        xxx[idx].append(i2 - i1)

safe_count = 0
for xx in xxx:
    safe_count += all(abs(x) <= 3 for x in xx) and (
        all(x > 0 for x in xx) or all(x < 0 for x in xx)
    )
print(safe_count)

# part 2
xxxx = [list() for _ in range(len(lines))]

for idx, line in enumerate(lines):
    line_perms = []
    for i in range(len(line)):
        new_line = line.copy()
        new_line.pop(i)
        line_perms.append(new_line)

    for line_perm in line_perms:
        xxx = []
        for i1, i2 in zip(line_perm[:-1], line_perm[1:]):
            xxx.append(i2 - i1)
        xxxx[idx].append(xxx)

safe_count = 0
for xxx in xxxx:
    safe_count_perms = 0
    for xx in xxx:
        safe_count_perms |= all(abs(x) <= 3 for x in xx) and (
            all(x > 0 for x in xx) or all(x < 0 for x in xx)
        )
    safe_count += safe_count_perms
print(safe_count)
