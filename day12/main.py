from typing import List
from copy import copy, deepcopy
# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi


def parse_file(file_name: str) -> List[List[str]]:
    f = open(file_name, 'r')
    heightmap = [[c for c in list(row)] for row in f.read().split('\n')[:-1]]
    return heightmap


POSSIBLE_SQUARES = [(0, 1, '>'), (0, -1, '<'), (1, 0, 'v'), (-1, 0, '^')]


# def get_square_value(square):
#     return

def find_start_square(heightmap, max_i, max_j):
    for i in range(max_i):
        for j in range(max_j):
            if heightmap[i][j] == 'S':
                return i, j


def log(message):
    # pass
    print(message)


def go_path(heightmap, start_i, start_j, old_visited_squares, old_arrows, path_lengths):
    max_i, max_j = len(heightmap), len(heightmap[0])
    i = start_i
    j = start_j
    visited_squares = copy(old_visited_squares)
    arrows = copy(old_arrows)
    done = False
    while not done:
        current_square = heightmap[i][j]
        current_square_value = ord(current_square) if current_square != 'S' else ord('a')
        visited_squares.add((i, j))
        if path_lengths and len(visited_squares) > min(path_lengths):
            break
        possible_next_squares = []
        for p in POSSIBLE_SQUARES:
            next_i = i + p[0]
            next_j = j + p[1]
            if not (0 <= next_i < max_i and 0 <= next_j < max_j):
                continue
            next_square = heightmap[next_i][next_j]
            next_square_value = ord(next_square) if next_square != 'E' else ord('z')
            if next_square_value - current_square_value not in [0, 1]:
                continue
            if (next_i, next_j) in visited_squares:
                continue
            if next_square == 'E':
                done = True
                break
            log(f'next_square: {next_square}')
            possible_next_squares.append((next_i, next_j, p[2]))

        if not possible_next_squares:
            log('No square to move :(')
            break

        if len(possible_next_squares) == 1:
            i, j, arrow = possible_next_squares[0]
            log(f'We go {arrow} to {i}, {j}')
            arrows[i][j] = arrow
        else:
            for possible_next_square in possible_next_squares:
                i, j, arrow = possible_next_square
                log(f'We go {arrow} to {i}, {j}')
                arrows[i][j] = arrow
                go_path(heightmap, i, j, visited_squares, arrows, path_lengths)
                # if done:
                #     break
    if done:
        path_lengths.add(len(visited_squares))
        print(len(visited_squares))
        # print(min(path_lengths))
        # print(len(visited_squares))
        # if len(visited_squares) < min(path_lengths):
        log('-'*20)
        for row in arrows:
            log(''.join(row))
        log('-'*20)
            # old_arrows = arrows

    return done


def solve_first():
    heightmap = parse_file('input.txt')
    max_i, max_j = len(heightmap), len(heightmap[0])
    i, j = find_start_square(heightmap, max_i, max_j)
    arrows = [['.' for _ in range(max_j)] for __ in range(max_i)]
    arrows[i][j] = 'S'
    path_lengths = set()
    visited_squares = set()
    done = go_path(heightmap, i, j, visited_squares, arrows, path_lengths)
    if done:
        log(f'We"ve found E!')
    else:
        log('We haven"t found E :(')
    print(min(path_lengths))
    # for row in arrows:
    #     log(''.join(row))


solve_first()
