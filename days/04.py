from itertools import product
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/04.actual")
example_input = parse_file("days/inputs/04.example")


def count_neighbours(grid: list[list[str]], position: tuple[int, int]) -> int:
    def check_position(position: tuple[int, int]) -> bool:
        (x, y) = position
        return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] == "@"

    (x, y) = position
    result = 0
    for dx, dy in product([-1, 0, 1], repeat=2):
        if (dx, dy) != (0, 0):
            result += 1 if check_position((x + dx, y + dy)) else 0
    return result


def test_count_neighbours():
    assert count_neighbours(list(map(list, example_input)), (0, 0)) == 2
    assert count_neighbours(list(map(list, example_input)), (2, 1)) == 6


def part_1(lines: list[str]) -> int:
    grid = list(map(list, lines))
    result = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == "@" and count_neighbours(grid, (x, y)) < 4:
                result += 1
    return result


def test_part_1_example():
    assert part_1(example_input) == 13


def test_part_1_actual():
    assert part_1(actual_input) == 1393


def part_2(lines: list[str]) -> int:
    grid = list(map(list, lines))
    result = 0
    while True:
        removed_in_loop = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "@" and count_neighbours(grid, (x, y)) < 4:
                    result += 1
                    removed_in_loop.append((x, y))
        if len(removed_in_loop) == 0:
            break
        else:
            for x, y in removed_in_loop:
                grid[y][x] = "x"
    return result


def test_part_2_example():
    assert part_2(example_input) == 43


def test_part_2_actual():
    assert part_2(actual_input) == 8643
