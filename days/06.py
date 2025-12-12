from functools import reduce
import operator
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/06.actual")
example_input = parse_file("days/inputs/06.example")

operators = {"+": operator.add, "*": operator.mul}


def part_1(lines: list[str]) -> int:
    data = list(list(int(x) for x in line.split()) for line in lines[:-1])
    result = 0
    for index, op in enumerate(lines[-1].split()):
        result += reduce(
            operators[op],
            (data[row][index] for row in range(len(lines) - 1)),
        )
    return result


def test_part_1_example():
    assert part_1(example_input) == 4277556


def test_part_1_actual():
    assert part_1(actual_input) == 5667835681547


def part_2(lines: list[str]) -> int:
    data = lines[:-1]
    parsed_numbers = []
    result = 0
    for x in range(len(lines[0]) - 1, -1, -1):
        number_found = False
        n = 0
        for y in range(len(data)):
            if lines[y][x] != " ":
                number_found = True
                n *= 10
                n += int(lines[y][x])
        if number_found:
            parsed_numbers.append(n)
        else:
            op = lines[-1][x + 1]
            result += reduce(operators[op], parsed_numbers)
            parsed_numbers = []
    # the last set of parsed numbers is not yet calculated
    result += reduce(operators[lines[-1][0]], parsed_numbers)
    return result


def test_part_2_example():
    assert part_2(example_input) == 3263827


def test_part_2_actual():
    assert part_2(actual_input) == 9434900032651
