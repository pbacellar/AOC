with open("input.txt", "r") as f:
    mat = f.readlines()


def look_hori_left_right(mat, i, j):
    if len(mat[i]) <= j + 3:
        return 0
    has_xmas = True
    for j, letter in zip(range(j + 1, j + 4), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_hori_right_left(mat, i, j):
    if j < 3:
        return 0
    has_xmas = True
    for j, letter in zip(range(j - 1, j - 4, -1), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_vert_up_down(mat, i, j):
    if len(mat) <= i + 3:
        return 0
    has_xmas = True
    for i, letter in zip(range(i + 1, i + 4), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_vert_down_up(mat, i, j):
    if i < 3:
        return 0
    has_xmas = True
    for i, letter in zip(range(i - 1, i - 4, -1), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_diag_down_left(mat, i, j):
    if len(mat) <= i + 3 or len(mat[i]) <= j + 3:
        return 0
    has_xmas = True
    for i, j, letter in zip(range(i + 1, i + 4), range(j + 1, j + 4), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_diag_down_right(mat, i, j):
    if len(mat) <= i + 3 or j < 3:
        return 0
    has_xmas = True
    for i, j, letter in zip(range(i + 1, i + 4), range(j - 1, j - 4, -1), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_diag_up_left(mat, i, j):
    if i < 3 or len(mat[i]) <= j + 3:
        return 0
    has_xmas = True
    for i, j, letter in zip(range(i - 1, i - 4, -1), range(j + 1, j + 4), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_diag_up_right(mat, i, j):
    if i < 3 or j < 3:
        return 0
    has_xmas = True
    for i, j, letter in zip(range(i - 1, i - 4, -1), range(j - 1, j - 4, -1), "MAS"):
        if mat[i][j] != letter:
            has_xmas = False
            break
    return int(has_xmas)


def look_around(mat, i, j):
    count = 0
    count += look_hori_left_right(mat, i, j)
    count += look_hori_right_left(mat, i, j)
    count += look_vert_up_down(mat, i, j)
    count += look_vert_down_up(mat, i, j)
    count += look_diag_down_left(mat, i, j)
    count += look_diag_down_right(mat, i, j)
    count += look_diag_up_left(mat, i, j)
    count += look_diag_up_right(mat, i, j)
    return count


count = 0
for i, line in enumerate(mat):
    for j in range(len(line)):
        if mat[i][j] == "X":
            count += look_around(mat, i, j)
print(count)


# Part 2
def part2_look_around(mat, i, j):
    if len(mat) <= i + 1 or len(mat[i]) <= j + 1:
        return 0
    if j < 1:
        return 0
    if i < 1:
        return 0

    # look up left and down right
    if not (
        (mat[i - 1][j - 1] == "M" and mat[i + 1][j + 1] == "S")
        or mat[i - 1][j - 1] == "S"
        and mat[i + 1][j + 1] == "M"
    ):
        return 0
    # look up right and down left
    if not (
        (mat[i - 1][j + 1] == "M" and mat[i + 1][j - 1] == "S")
        or mat[i - 1][j + 1] == "S"
        and mat[i + 1][j - 1] == "M"
    ):
        return 0

    return 1


count = 0
for i, line in enumerate(mat):
    for j in range(len(line)):
        if mat[i][j] == "A":
            count += part2_look_around(mat, i, j)
print(count)
