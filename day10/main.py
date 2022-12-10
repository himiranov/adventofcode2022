import math
from typing import List


def parse_file(file_name: str) -> List[str]:
    f = open(file_name, 'r')
    rows = [row for row in f.read().split('\n')[:-1]]
    return rows


def solve_first():
    rows = parse_file('input.txt')
    cycle = 0
    signal_strength = 0
    x = 1
    check_cycle = 20
    check_cycle_step = 40
    for row in rows:
        instruction = row.split(' ')
        if instruction[0] == 'noop':
            cycle += 1
            continue
        if instruction[0] == 'addx':
            cycle += 2
            if cycle >= check_cycle:
                signal_strength += x * check_cycle
                print(f'Cycle: {check_cycle}, x: {x}, check_cycle: {check_cycle}, signal_strength: {signal_strength}')
                check_cycle += check_cycle_step

            x += int(instruction[1])
    print(signal_strength)


def update_crt_row(cycle: int, x: int, crt_row: str, crt_row_length: int) -> str:
    if x <= cycle <= x + 2:
        crt_row += '#'
    else:
        crt_row += '.'
    if len(crt_row) == crt_row_length:
        print(crt_row)
        crt_row = ''
    return crt_row


def solve_second():
    rows = parse_file('input.txt')
    cycle = 1
    x = 1
    crt_row_length = 40
    crt_row = ''
    for row in rows:
        crt_row = update_crt_row(cycle, x, crt_row, crt_row_length)
        if not crt_row:
            cycle = 0
        instruction = row.split(' ')
        if instruction[0] == 'noop':
            cycle += 1
        elif instruction[0] == 'addx':
            cycle += 1
            crt_row = update_crt_row(cycle, x, crt_row, crt_row_length)
            if not crt_row:
                cycle = 0
            cycle += 1
            x += int(instruction[1])


def solve_second_2():
    rows = parse_file('input.txt')
    instructions = []
    for row in rows:
        instruction = row.split(' ')
        if instruction[0] == 'noop':
            instructions.append(0)
        elif instruction[0] == 'addx':
            instructions.append(0)
            instructions.append(int(instruction[1]))

    cycle = 1
    x = 1
    crt_row_length = 40
    crt_row = ''
    for i in instructions:
        if x <= cycle <= x + 2:
            crt_row += '#'
        else:
            crt_row += '.'

        if len(crt_row) == crt_row_length:
            print(crt_row)
            crt_row = ''
            cycle = 0

        cycle += 1
        x += i

    print(crt_row)


solve_first()
print('')
print('-'*40)
print('')
solve_second()
print('')
print('-'*40)
print('')
solve_second_2()
