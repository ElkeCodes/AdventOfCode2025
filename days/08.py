from functools import reduce
from itertools import combinations
from math import sqrt
from typing import Tuple, cast
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/08.actual")
example_input = parse_file("days/inputs/08.example")


def get_distance(one: tuple[int, int, int], other: tuple[int, int, int]) -> float:
    (x1, y1, z1) = one
    (x2, y2, z2) = other
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(lines: list[str]):
    return list(
        cast(Tuple[int, int, int], tuple(map(int, line.split(",")))) for line in lines
    )


def part_1(lines: list[str], limit) -> int:
    parsed_coordinates = parse_coordinates(lines)
    circuits = {
        i: {
            coordinate,
        }
        for i, coordinate in enumerate(parsed_coordinates)
    }
    count = 0
    for one, other, _ in sorted(
        map(
            lambda coords: (
                coords[0],
                coords[1],
                get_distance(coords[0], coords[1]),
            ),
            combinations(parsed_coordinates, 2),
        ),
        key=lambda x: x[2],
    ):
        if count == limit:
            break
        one_id = -1
        other_id = -1
        for circuit_id in circuits:
            if one in circuits[circuit_id]:
                one_id = circuit_id
            if other in circuits[circuit_id]:
                other_id = circuit_id
        count += 1
        if one_id != other_id:
            circuits[one_id] |= circuits[other_id]
            del circuits[other_id]
    return reduce(
        lambda x, y: x * y,
        map(
            lambda circuit_id: len(circuits[circuit_id]),
            sorted(circuits, key=lambda k: len(circuits[k]), reverse=True)[:3],
        ),
    )


def test_part_1_example():
    assert part_1(example_input, 10) == 40


def test_part_1_actual():
    assert part_1(actual_input, 1000) == 79056


def part_2(lines: list[str]) -> int:
    parsed_coordinates = parse_coordinates(lines)
    circuits = {
        i: {
            coordinate,
        }
        for i, coordinate in enumerate(parsed_coordinates)
    }
    count = 0
    for one, other, _ in sorted(
        map(
            lambda coords: (
                coords[0],
                coords[1],
                get_distance(coords[0], coords[1]),
            ),
            combinations(parsed_coordinates, 2),
        ),
        key=lambda x: x[2],
    ):
        one_id = -1
        other_id = -1
        amount_of_circuits = 0
        for circuit_id in circuits:
            amount_of_circuits += 1
            if one in circuits[circuit_id]:
                one_id = circuit_id
            if other in circuits[circuit_id]:
                other_id = circuit_id
        count += 1
        if one_id != other_id:
            circuits[one_id] |= circuits[other_id]
            del circuits[other_id]
            # if there were 2 circuits before we merged them,
            # we had the final connection
            if amount_of_circuits == 2:
                return one[0] * other[0]
    raise Exception("This should be unreachable")


def test_part_2_example():
    assert part_2(example_input) == 25272


def test_part_2_actual():
    assert part_2(actual_input) == 4639477
