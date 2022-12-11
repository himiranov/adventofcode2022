from collections import defaultdict
from typing import List

# Monkey 0:
# Starting items: 79, 98
# Operation: new = old * 19
# Test: divisible by 23
# If true: throw to monkey 2
# If false: throw to monkey 3


def parse_monkey(data):
    monkey = {
        'id': int(data[0].split(' ')[1][:-1]),
        'items': [
            int(item[:-1])
            if item.endswith(',')
            else int(item)
            for item in data[1].strip().split(' ')[2:]
        ],
        'operation': data[2].strip().split(' ')[3:],
        'divisible_test': int(data[3].strip().split(' ')[-1]),
        'true': int(data[4].strip().split(' ')[-1]),
        'false': int(data[5].strip().split(' ')[-1]),
        'inspected_items': 0
    }
    return monkey


def parse_file(file_name: str) -> List[dict]:
    f = open(file_name, 'r')
    rows = f.read().split('\n')[:-1]
    monkeys_map = {}
    monkeys = []
    i = 0
    while i <= len(rows) - 6:
        monkey = parse_monkey(rows[i: i+6])
        monkeys_map[monkey['id']] = monkey
        monkeys.append(monkey)
        i += 7

    return monkeys


OPERATIONS_MAP = {
    '*': lambda x,y: x * y,
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '/': lambda x,y: x / y,
}


def solve_first():
    monkeys = parse_file('input.txt')
    rounds = 20
    for i in range(rounds):
        for monkey in monkeys:
            left, operator, right = monkey['operation']
            operator_func = OPERATIONS_MAP[operator]
            for item in monkey['items']:
                x = item
                if right == 'old':
                    y = item
                else:
                    y = int(right)
                new_item = operator_func(x, y)
                new_item = new_item // 3
                if new_item % monkey['divisible_test'] == 0:
                    monkeys[monkey['true']]['items'].append(new_item)
                else:
                    monkeys[monkey['false']]['items'].append(new_item)
                monkey['inspected_items'] += 1
            monkey['items'] = []

    inspected_items = sorted([m['inspected_items'] for m in monkeys], reverse=True)
    print(inspected_items[0] * inspected_items[1])


def get_operation(operator, right):
    operator_func = OPERATIONS_MAP[operator]

    def inner(item):
        return (
            operator_func(item, int(right))
            if right != 'old'
            else operator_func(item, item)
        )

    return inner


def solve_second():
    monkeys = parse_file('input.txt')
    rounds = 10000
    inspected_items_map = defaultdict(int)
    monkey_to_action = {}
    items = []
    initial_items_to_monkey_id = {}
    common_div = 1
    for monkey in monkeys:
        monkey_id = monkey['id']
        left, operator, right = monkey['operation']
        monkey_action = get_operation(operator, right)
        common_div *= monkey['divisible_test']
        monkey_to_action[monkey_id] = monkey_action
        for item in monkey['items']:
            item_key = (item, monkey_id)
            items.append(item_key)
            initial_items_to_monkey_id[item_key] = monkey

    for i in range(rounds):
        new_item_keys = []
        for item_key in items:
            item, monkey_id = item_key
            current_monkey = monkeys[monkey_id]
            inspected_items_map[current_monkey['id']] += 1
            action = monkey_to_action[current_monkey['id']]
            new_item = action(item)
            if new_item > common_div:
                new_item %= common_div
            if new_item % current_monkey['divisible_test'] == 0:
                current_monkey = monkeys[current_monkey['true']]
            else:
                current_monkey = monkeys[current_monkey['false']]
            new_item_key = (new_item, current_monkey['id'])
            if monkey_id < current_monkey['id']:
                items.append(new_item_key)
            else:
                new_item_keys.append(new_item_key)
        items = new_item_keys

    inspected_items = sorted(inspected_items_map.values(), reverse=True)
    print(inspected_items[0] * inspected_items[1])


solve_first()
solve_second()
