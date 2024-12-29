import sys
sys.setrecursionlimit(10_000)
print(sys.getrecursionlimit())

with open("input.txt", "r") as f:
    mat = [[c for c in x] for x in f.read().splitlines()]
# print(mat)

# input_ ="""89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""
# mat = [[c for c in x] for x in input_.splitlines()]


class Node:
    def __init__(self, value, i, j, adjacent):
        self.value = value
        self.i = i
        self.j = j
        self.adjacent = adjacent

    def __eq__(self, other) -> bool:
        return self.i == other.i and self.j == other.j

    def __hash__(self) -> int:
        return hash(str(self.i) + str(self.j))

    def __str__(self):
        return f"node {self.value}: {self.i}, {self.j}   Adjacent nodes: {len(self.adjacent)}"


def insert_unique_list(item, lst: list):
    try:
        i = lst.index(item)
    except ValueError:
        lst.append(item)
        return item
    return lst[i]


def get_adjcent_nodes(mat, i, j, nodes=None):
    nodes = nodes or []
    adjacent_nodes = []
    if i-1 >= 0:
        try:
            idx = nodes.index(Node(mat[i-1][j], i-1, j, []))
            adjacent_nodes.append(nodes[idx])
        except ValueError:
            it = insert_unique_list(Node(mat[i-1][j], i-1, j, []), nodes)
            adjacents = get_adjcent_nodes(mat, i-1, j, nodes)
            it.adjacent = adjacents
            adjacent_nodes.append(it)
    if j-1 >= 0:
        try:
            idx = nodes.index(Node(mat[i][j-1], i, j-1, []))
            adjacent_nodes.append(nodes[idx])
        except ValueError:
            it = insert_unique_list(Node(mat[i][j-1], i, j-1, []), nodes)
            adjacents = get_adjcent_nodes(mat, i, j-1, nodes)
            it.adjacent = adjacents
            adjacent_nodes.append(it)
    if i+1 < len(mat):
        try:
            idx = nodes.index(Node(mat[i+1][j], i+1, j, []))
            adjacent_nodes.append(nodes[idx])
        except ValueError:
            it = insert_unique_list(Node(mat[i+1][j], i+1, j, []), nodes)
            adjacents = get_adjcent_nodes(mat, i+1, j, nodes)
            it.adjacent = adjacents
            adjacent_nodes.append(it)
    if j+1 < len(mat[0]):
        try:
            idx = nodes.index(Node(mat[i][j+1], i, j+1, []))
            adjacent_nodes.append(nodes[idx])
        except ValueError:
            it = insert_unique_list(Node(mat[i][j+1], i, j+1, []), nodes)
            adjacents = get_adjcent_nodes(mat, i, j+1, nodes)
            it.adjacent = adjacents
            adjacent_nodes.append(it)
    return adjacent_nodes


def get_nodes(mat, i, j, nodes=None):
    nodes = nodes or []
    n0 = Node(mat[i][j], i, j, [])
    nodes.append(n0)
    n0.adjacent = get_adjcent_nodes(mat, i, j, nodes)
    _ = insert_unique_list(n0, nodes)
    return nodes


nodes = get_nodes(mat, 0, 0)
# print(len(nodes))
# [print(str(node) + "  " + str([str(n) for n in node.adjacent])) for node in nodes]


def bfs_aux(nodes):
    score = 0
    for node in nodes:
        if node.value == "0":
            plus_score = bfs(node, score=0, visited=[node])
            # if plus_score:
                # print(node, "       ", plus_score)
            score += plus_score
    return score


def bfs(node, score=0, visited=None):
    visited = visited or []
    for adj in node.adjacent:
        if adj.value == str(int(node.value) + 1):
            if adj.value == "9" and adj not in visited:
                # print(node, adj)
                # TODO part 2 comment this line
                visited.append(adj)
                score = score + 1
            score += bfs(adj, 0, visited)
    return score

print("Start search")
print(bfs_aux(nodes))
