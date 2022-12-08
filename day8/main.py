def parse_file() -> tuple[list[list[int]], list[list[int]]]:
    f = open('input.txt', 'r')
    tree_map_rows = [[int(tree) for tree in list(row)] for row in f.read().split('\n')[:-1]]
    tree_map_columns = [[tree_map_rows[i][j] for i in range(len(tree_map_rows))] for j in range(len(tree_map_rows[0]))]
    return tree_map_rows, tree_map_columns


def solve_first():
    tree_map_rows, tree_map_columns = parse_file()
    visible_count = len(tree_map_rows) * 2 + (len(tree_map_rows[0]) - 2) * 2
    for i, row in enumerate(tree_map_rows[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            if (
                max(tree_map_rows[i][:j]) < tree or
                max(tree_map_rows[i][j+1:]) < tree or
                max(tree_map_columns[j][:i]) < tree or
                max(tree_map_columns[j][i+1:]) < tree
            ):
                visible_count += 1
    print(visible_count)


def check_viewing_distance(tree: int, next_to_it_trees: list[int]) -> int:
    distance = 0
    for next_to_it_tree in next_to_it_trees:
        distance += 1
        if next_to_it_tree >= tree:
            break
    return distance


def solve_second():
    tree_map_rows, tree_map_columns = parse_file()
    distance = 0
    for i, row in enumerate(tree_map_rows[1:-1], start=1):
        for j, tree in enumerate(row[1:-1], start=1):
            current_distance = (
                check_viewing_distance(tree, list(reversed(tree_map_rows[i][:j]))) *
                check_viewing_distance(tree, tree_map_rows[i][j+1:]) *
                check_viewing_distance(tree, list(reversed(tree_map_columns[j][:i]))) *
                check_viewing_distance(tree, tree_map_columns[j][i+1:])
            )
            distance = max(current_distance, distance)

    print(distance)


solve_first()
solve_second()
