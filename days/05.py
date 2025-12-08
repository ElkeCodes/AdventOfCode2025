from utils.parse_file import parse_file
from typing import cast, Tuple

actual_input = parse_file("days/inputs/05.actual")
example_input = parse_file("days/inputs/05.example")


def parse_lines(lines: list[str]):
    split = lines.index("")
    ranges = list(
        map(
            lambda line: cast(Tuple[int, int], tuple(int(x) for x in line.split("-"))),
            lines[0:split],
        )
    )
    ids = list(int(x) for x in lines[(split + 1) :])
    return (ranges, ids)


def part_1(lines: list[str]) -> int:
    (ranges, ids) = parse_lines(lines)
    return sum(any(start <= id <= end for (start, end) in ranges) for id in ids)


def test_part_1_example():
    assert part_1(example_input) == 3


def test_part_1_actual():
    assert part_1(actual_input) == 607


def part_2(lines: list[str]) -> int:
    (ranges, _) = parse_lines(lines)
    sorted_ranges = sorted(ranges)
    previous_end = 0
    result = 0
    for start, end in sorted_ranges:
        if end <= previous_end:
            continue
        if start <= previous_end:
            result += end - previous_end
        else:
            result += end - start + 1
        previous_end = max(end, previous_end)
    return result


def test_part_2_example():
    assert part_2(example_input) == 14


def test_part_2_actual():
    assert part_2(actual_input) == 342433357244012
