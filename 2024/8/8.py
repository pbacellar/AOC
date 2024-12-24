with open("input.txt", "r") as f:
    mat = [[c for c in l] for l in f.read().splitlines()]


def print_mat(mat):
    for line in mat:
        print("".join(line))
    print()


def find_next_antennas(mat, curr_antenna_i, curr_antenna_j):
    if curr_antenna_i >= len(mat) or curr_antenna_j >= len(mat[0]):
        return []
    next_antennas_positions = []
    for i in range(curr_antenna_i, len(mat)):
        for j in range(0, len(mat[0])):
            if (i, j) <= (curr_antenna_i, curr_antenna_j):
                continue
            if mat[i][j] == mat[curr_antenna_i][curr_antenna_j]:
                next_antennas_positions.append((i, j))
    return next_antennas_positions


def is_antinode_out_of_bounds(mat, antenna):
    return (
        antenna[0] < 0
        or antenna[1] < 0
        or antenna[0] >= len(mat)
        or antenna[1] >= len(mat[antenna[0]])
    )


def find_antinodes_for_antenna_pair(mat, antenna1, antenna2):
    dist_i = antenna1[0] - antenna2[0]
    dist_j = antenna1[1] - antenna2[1]

    i_antinode_1 = antenna1[0] + dist_i
    j_antinode_1 = antenna1[1] + dist_j

    i_antinode_2 = antenna2[0] - dist_i
    j_antinode_2 = antenna2[1] - dist_j

    antinodes = []
    if not is_antinode_out_of_bounds(mat, (i_antinode_1, j_antinode_1)):
        antinodes.append((i_antinode_1, j_antinode_1))
    if not is_antinode_out_of_bounds(mat, (i_antinode_2, j_antinode_2)):
        antinodes.append((i_antinode_2, j_antinode_2))
    return antinodes


print_mat(mat)

antinodes_mat = [["." for _ in range(len(mat[0]))] for _ in range(len(mat))]

sum_ = 0
found_antinodes = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] != ".":
            next_antennas = find_next_antennas(mat, i, j)
            for next_antenna in next_antennas:
                antinodes = find_antinodes_for_antenna_pair(mat, (i, j), next_antenna)
                for antinode in antinodes:
                    if antinode not in found_antinodes:
                        sum_ += 1
                    found_antinodes.append(antinode)
                    antinodes_mat[antinode[0]][antinode[1]] = "#"     

print_mat(antinodes_mat)
print(sum_)

# Part 2


def find_antinodes_for_antenna_pair2(mat, antenna1, antenna2):
    dist_i = antenna1[0] - antenna2[0]
    dist_j = antenna1[1] - antenna2[1]

    orig_dist_i = dist_i
    orig_dist_j = dist_j

    antinodes = []
    OFB = False
    while not OFB:
        i_antinode_1 = antenna1[0] + dist_i
        j_antinode_1 = antenna1[1] + dist_j
        if not is_antinode_out_of_bounds(mat, (i_antinode_1, j_antinode_1)):
            antinodes.append((i_antinode_1, j_antinode_1))
        else:
            OFB = True
        dist_i += orig_dist_i
        dist_j += orig_dist_j

    OFB = False
    dist_i = antenna1[0] - antenna2[0]
    dist_j = antenna1[1] - antenna2[1]
    while not OFB:
        i_antinode_2 = antenna2[0] - dist_i
        j_antinode_2 = antenna2[1] - dist_j
        if not is_antinode_out_of_bounds(mat, (i_antinode_2, j_antinode_2)):
            antinodes.append((i_antinode_2, j_antinode_2))
        else:
            OFB = True
        dist_i += orig_dist_i
        dist_j += orig_dist_j

    return antinodes


print_mat(mat)

antinodes_mat = [["." for _ in range(len(mat[0]))] for _ in range(len(mat))]

sum_ = 0
found_antinodes = []
found_antennas = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] != ".":
            if(i, j) not in found_antennas:
                found_antennas.append((i, j))
for i in range(len(mat)):
    for j in range(len(mat[0])):
        if mat[i][j] != ".":
            sum_ += 1
            antinodes_mat[i][j] = mat[i][j]
            next_antennas = find_next_antennas(mat, i, j)
            antenna_sum = 0
            for next_antenna in next_antennas:
                antinodes = find_antinodes_for_antenna_pair2(mat, (i, j), next_antenna)
                for antinode in antinodes:
                    if antinode not in found_antinodes and antinode not in found_antennas:
                        antenna_sum += 1
                        sum_ += 1
                    found_antinodes.append(antinode)
                    if antinode not in found_antennas:
                        antinodes_mat[antinode[0]][antinode[1]] = "#"

print_mat(antinodes_mat)
print(sum_)
