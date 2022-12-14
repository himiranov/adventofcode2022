from typing import List

# [1,1,3,1,1]
# [1,1,5,1,1]


def parse_file(file_name: str) -> List[str]:
    f = open(file_name, 'r')
    return [row for row in f.read().split('\n')[:-1]]


def check_is_right_order(packet1, packet2):
    if not isinstance(packet1, list):
        packet1 = [packet1]
    if not isinstance(packet2, list):
        packet2 = [packet2]
    for i in range(len(packet1)):
        if i >= len(packet2):
            return 0

        if isinstance(packet1[i], list) or isinstance(packet2[i], list):
            is_sub_list_right = check_is_right_order(packet1[i], packet2[i])
            if is_sub_list_right == -1:
                continue
            return is_sub_list_right

        if packet1[i] < packet2[i]:
            return 1
        if packet1[i] > packet2[i]:
            return 0

    if len(packet1) < len(packet2):
        return 1

    return -1


def solve_first():
    rows = parse_file('input.txt')
    packets_pair_number = 0
    sum_of_numbers = 0
    for i in range(0, len(rows), 3):
        packets_pair_number += 1
        if check_is_right_order(eval(rows[i]), eval(rows[i+1])):
            sum_of_numbers += packets_pair_number

    print(f'#1: {sum_of_numbers}')


def solve_second():
    rows = parse_file('input.txt')
    packets = [[[2]], [[6]]]
    for i in range(0, len(rows), 3):
        packets.append(eval(rows[i]))
        packets.append(eval(rows[i+1]))

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(packets) - 1):
            if not check_is_right_order(packets[i], packets[i+1]):
                packets[i], packets[i+1] = packets[i+1], packets[i]
                swapped = True

    result = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)
    print(f'#2: {result}')


solve_first()
solve_second()
