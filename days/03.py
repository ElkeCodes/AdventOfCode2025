from itertools import combinations
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/03.actual")
example_input = parse_file("days/inputs/03.example")


def get_largest_joltage(bank: str, batteries: int) -> int:
    return max(map(int, map(lambda x: x[0] + x[1], combinations(bank, batteries))))


def part_1(lines: list[str]) -> int:
    return sum(map(lambda bank: get_largest_joltage(bank, 2), lines))


def test_part_1():
    assert part_1(actual_input) == 17524


def test_part_1_example():
    assert part_1(example_input) == 357


# def part_2(lines: list[str]) -> int:
#     return sum(map(lambda bank: get_largest_joltage(bank, 12), lines))


# def test_part_2():
#     assert part_2(actual_input) == 17524


# def test_part_2_example():
#     assert part_2(example_input) == 3121910778619
