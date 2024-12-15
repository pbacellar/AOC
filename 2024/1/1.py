with open("input.txt", "r") as f:
    lines = f.readlines()


l1 = []
l2 = []
for line in lines:
    l1.append(int(line.split()[0]))
    l2.append(int(line.split()[1]))

l1 = sorted(l1)
l2 = sorted(l2)


sum_ = 0
for i1, i2 in zip(l1, l2):
    sum_ += abs(i1 - i2)

print(sum_)

sim_score = 0

for i1 in l1:
    sim_score += i1 * l2.count(i1)

print(sim_score)

l1_dup_count = [(i, l1.count(i)) for i in l1 if l1.count(i) > 1]
print(l1_dup_count)

l2_dup_count = [(i, l2.count(i)) for i in l2 if l2.count(i) > 1]
print(l2_dup_count)
print(len(l2) - len(l2_dup_count))

print(len(l1))
print(len(l2))
