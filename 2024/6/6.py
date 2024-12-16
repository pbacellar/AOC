from copy import deepcopy

with open("input.txt", "r") as f:
    mat = [[c for c in cs] for cs in f.read().splitlines()]


def print_mat(mat):
    for row in mat:
        print("".join(row))
    print()


def find_soldier(mat) -> tuple[int, int]:
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "^":
                return i, j


def walk_up(mat, i, j):
    if i == 0:
        mat[i][j] = "X"
        return False, -1, -1, True
    if mat[i-1][j] in ["#", "O"]:
        mat[i][j] = ">"
        return ("^", i-1, j), i, j, False
    mat[i][j] = "X"
    mat[i-1][j] = "^"
    return False, i-1, j, False


def walk_right(mat, i, j):
    if j == len(mat[i]) - 1:
        mat[i][j] = "X"
        return False, -1, -1, True
    if mat[i][j+1] in ["#", "O"]:
        mat[i][j] = "V"
        return (">", i, j+1), i, j, False
    mat[i][j] = "X"
    mat[i][j+1] = ">"
    return False, i, j+1, False


def walk_down(mat, i, j):
    if i == len(mat) - 1:
        mat[i][j] = "X"
        return False, -1, -1, True
    if mat[i+1][j] in ["#", "O"]:
        mat[i][j] = "<"
        return ("V", i+1, j), i, j, False
    mat[i][j] = "X"
    mat[i+1][j] = "V"
    return False, i+1, j, False


def walk_left(mat, i, j):
    if j == 0:
        mat[i][j] = "X"
        return False, -1, -1, True
    if mat[i][j-1] in ["#", "O"]:
        mat[i][j] = "^"
        return ("<", i, j-1), i, j, False
    mat[i][j] = "X"
    mat[i][j-1] = "<"
    return False, i, j-1, False


def walk_path(mat, i, j):
    mat = deepcopy(mat)
    obstacles_hit = []
    ofb = False
    while not ofb:
        if mat[i][j] == "^":
            obstacle_coord, i, j, ofb = walk_up(mat, i, j)
            if obstacle_coord in obstacles_hit:
                return mat, "loop", obstacles_hit
            obstacles_hit.append(obstacle_coord) if obstacle_coord else None
            continue
        if mat[i][j] == ">":
            obstacle_coord, i, j, ofb = walk_right(mat, i, j)
            if obstacle_coord in obstacles_hit:
                return mat, "loop", obstacles_hit
            obstacles_hit.append(obstacle_coord) if obstacle_coord else None
            continue
        if mat[i][j] == "V":
            obstacle_coord, i, j, ofb = walk_down(mat, i, j)
            if obstacle_coord in obstacles_hit:
                return mat, "loop", obstacles_hit
            obstacles_hit.append(obstacle_coord) if obstacle_coord else None
            continue
        if mat[i][j] == "<":
            obstacle_coord, i, j, ofb = walk_left(mat, i, j)
            if obstacle_coord in obstacles_hit:
                return mat, "loop", obstacles_hit
            obstacles_hit.append(obstacle_coord) if obstacle_coord else None
    return mat, "no_loop", obstacles_hit


i, j = find_soldier(mat)
mat, _, _ = walk_path(mat, i, j)

sum_ = 0
for row in mat:
    for c in row:
        if c == "X":
            sum_ += 1
print(sum_)

# part 2


def obstacle_in_path(mat, i, j, dir):
    if dir == "^":
        for k in range(i-1, -1, -1):
            if mat[k][j] in ["#", "O"]:
                return True
    if dir == ">":
        for k in range(j+1, len(mat[i])):
            if mat[i][k] in ["#", "O"]:
                return True
    if dir == "V":
        for k in range(i+1, len(mat)):
            if mat[k][j] in ["#", "O"]:
                return True
    if dir == "<":
        for k in range(j-1, -1, -1):
            if mat[i][k] in ["#", "O"]:
                return True
    return False


def walk_path2(mat, i, j):
    obstacles_hit = []
    ofb = False
    loop_count = 0
    walked_paths = []
    while not ofb:
        # print(i, j, mat[i][j])
        walked_paths.append((i, j))
        # print_mat(mat)
        if mat[i][j] == "^":
            if obstacle_in_path(mat, i, j, ">") and i != 0 and mat[i-1][j] != "#" and (i-1, j) not in walked_paths:
                mat_test = deepcopy(mat)
                mat_test[i-1][j] = "O"
                mat_test, loop, obstacles_hit = walk_path(mat_test, i, j)
                if loop == "loop":
                    # print(i, j)
                    # print_mat(mat_test)
                    loop_count += 1
            obstacle_coord, i, j, ofb = walk_up(mat, i, j)
            continue
        if mat[i][j] == ">":
            if obstacle_in_path(mat, i, j, "V") and j != len(mat[i]) - 1 and mat[i][j+1] != "#" and (i, j+1) not in walked_paths:
                mat_test = deepcopy(mat)
                mat_test[i][j+1] = "O"
                mat_test, loop, obstacles_hit = walk_path(mat_test, i, j)
                if loop == "loop":
                    # print(i, j)
                    # print_mat(mat_test)
                    loop_count += 1
            obstacle_coord, i, j, ofb = walk_right(mat, i, j)
            continue
        if mat[i][j] == "V":
            if obstacle_in_path(mat, i, j, "<") and i != len(mat) - 1 and mat[i+1][j] != "#" and (i+1, j) not in walked_paths:
                mat_test = deepcopy(mat)
                mat_test[i+1][j] = "O"
                mat_test, loop, obstacles_hit = walk_path(mat_test, i, j)
                if loop == "loop":
                    # print(i, j)
                    # print_mat(mat_test)
                    loop_count += 1
            obstacle_coord, i, j, ofb = walk_down(mat, i, j)
            continue
        if mat[i][j] == "<":
            # print(walked_paths)
            if obstacle_in_path(mat, i, j, "^") and j != 0 and mat[i][j-1] != "#" and (i, j-1) not in walked_paths:
                mat_test = deepcopy(mat)
                mat_test[i][j-1] = "O"
                mat_test, loop, obstacles_hit = walk_path(mat_test, i, j)
                if loop == "loop":
                    # print(i, j)
                    # print_mat(mat_test)
                    loop_count += 1
            obstacle_coord, i, j, ofb = walk_left(mat, i, j)
    return loop_count


with open("input.txt", "r") as f:
    mat = [[c for c in cs] for cs in f.read().splitlines()]
i, j = find_soldier(mat)
print(walk_path2(mat, i, j))
