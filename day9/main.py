import math
from typing import List


class Point:
    def __init__(self, name: str, x: int = 1, y: int = 1):
        self.x = x
        self.y = y
        self.name = name

    def is_touched(self, point: 'Point') -> bool:
        return (
            math.fabs(point.x - self.x) <= 1 and
            math.fabs(point.y - self.y) <= 1
        )

    def touch_point(self, point: 'Point') -> None:
        if self.is_touched(point):
            return

        if point.x < self.x:
            self.x -= 1
        elif point.x > self.x:
            self.x += 1

        if point.y < self.y:
            self.y -= 1
        elif point.y > self.y:
            self.y += 1


DIRECTIONS = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1),
}


def parse_file(file_name: str) -> List[str]:
    f = open(file_name, 'r')
    rows = [row for row in f.read().split('\n')[:-1]]
    return rows


def draw_map(points: List[Point], min: int = -30, max: int = 30) -> None:
    points_map = {(p.x, p.y): p for p in points}
    lines = []
    for i in range(min, max, 1):
        line = ''
        for j in range(min, max, 1):
            if p := points_map.get((j, i)):
                line += p.name
            else:
                line += '.'
        lines.append(line)

    for line in reversed(lines):
        print(line)


def solve_first():
    rows = parse_file('input.txt')
    visited_positions = set()
    head = Point('H')
    tail = Point('T')
    for row in rows:
        direction, steps_count = row.split(' ')
        for i in range(int(steps_count)):
            head_x_prev = head.x
            head_y_prev = head.y
            head.x += DIRECTIONS[direction][0]
            head.y += DIRECTIONS[direction][1]
            if not tail.is_touched(head):
                tail.x = head_x_prev
                tail.y = head_y_prev
            visited_positions.add((tail.x, tail.y))

    print(len(visited_positions))


def solve_second():
    rows = parse_file('input.txt')
    visited_positions = set()
    head = Point('H')
    points = [head]
    points.extend([Point(str(i)) for i in range(1, 10)])
    tail = points[-1]
    for row in rows:
        direction, steps_count = row.split(' ')
        for i in range(int(steps_count)):
            head.x += DIRECTIONS[direction][0]
            head.y += DIRECTIONS[direction][1]
            prev_point = head
            for point in points[1:]:
                point.touch_point(prev_point)
                prev_point = point

            visited_positions.add((tail.x, tail.y))
    print(len(visited_positions))
    print(draw_map(points, -90, 30))


solve_first()
solve_second()
