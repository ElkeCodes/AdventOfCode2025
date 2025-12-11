from itertools import chain, combinations, pairwise
from typing import Tuple, cast
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/09.actual")
example_input = parse_file("days/inputs/09.example")


def parse_coordinates(lines: list[str]):
    return list(
        cast(Tuple[int, int], tuple(map(int, line.split(",")))) for line in lines
    )


def get_area(one: tuple[int, int], other: tuple[int, int]) -> int:
    return (abs(other[1] - one[1]) + 1) * (abs(other[0] - one[0]) + 1)


def test_get_area():
    assert get_area((2, 5), (9, 7)) == 24
    assert get_area((7, 1), (11, 7)) == 35
    assert get_area((7, 3), (2, 3)) == 6
    assert get_area((2, 5), (11, 1)) == 50


def part_1(lines: list[str]) -> int:
    coordinates = parse_coordinates(lines)
    max_size = 0
    for one, other in combinations(coordinates, 2):
        max_size = max(max_size, get_area(one, other))
    return max_size


def test_part_1_example():
    assert part_1(example_input) == 50


def test_part_1_actual():
    assert part_1(actual_input) == 4735268538


def get_edges(
    coordinates: list[tuple[int, int]],
) -> pairwise[tuple[tuple[int, int], tuple[int, int]]]:
    return pairwise(chain(coordinates, [coordinates[0]]))


def test_get_edges():
    assert list(
        get_edges(
            [
                (7, 1),
                (11, 1),
                (11, 7),
                (9, 7),
                (9, 5),
                (2, 5),
                (2, 3),
                (7, 3),
            ]
        )
    ) == [
        (
            (7, 1),
            (11, 1),
        ),
        (
            (11, 1),
            (11, 7),
        ),
        (
            (11, 7),
            (9, 7),
        ),
        (
            (9, 7),
            (9, 5),
        ),
        (
            (9, 5),
            (2, 5),
        ),
        (
            (2, 5),
            (2, 3),
        ),
        (
            (2, 3),
            (7, 3),
        ),
        ((7, 3), (7, 1)),
    ]


def part_2(puzzle_input):
    coordinates = parse_coordinates(puzzle_input)
    max_size = 0
    sorted_edges = list(map(sorted, sorted(get_edges(list(coordinates)))))
    for (one_x, one_y), (other_x, other_y) in combinations(coordinates, 2):
        (one_x, one_y), (other_x, other_y) = sorted(
            ((one_x, one_y), (other_x, other_y))
        )
        one_y, other_y = sorted((one_y, other_y))
        if not any(
            (
                edge_other_x > one_x
                and edge_one_x < other_x
                and edge_other_y > one_y
                and edge_one_y < other_y
            )
            for (edge_one_x, edge_one_y), (edge_other_x, edge_other_y) in sorted_edges
        ):
            max_size = max(get_area((one_x, one_y), (other_x, other_y)), max_size)
    return max_size


def test_part_2_example():
    assert part_2(example_input) == 24


def test_part_2_actual():
    #     assert part_2(actual_input) == 4595056840 # too high
    assert part_2(actual_input) == 1537458069
