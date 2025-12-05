from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/01.actual")
example_input = parse_file("days/inputs/01.example")


def part_1(lines: list[str]) -> int:
    position = 50
    times_0 = 0
    for line in lines:
        direction, amount = line[0], int(line[1:])
        match direction:
            case "R":
                position += amount
            case "L":
                position -= amount
        position %= 100
        if position == 0:
            times_0 += 1
    return times_0


def test_part_1():
    assert part_1(actual_input) == 1139


def test_part_1_example():
    assert part_1(example_input) == 3


def part_2(lines: list[str]) -> int:
    position = 50
    times_0 = 0
    for line in lines:
        direction, amount = line[0], int(line[1:])
        for _ in range(amount):
            match direction:
                case "R":
                    position += 1
                case "L":
                    position -= 1
            position %= 100
            times_0 += position == 0
    return times_0


def test_part_2():
    assert part_2(actual_input) == 6684


def test_part_2_example():
    assert part_2(example_input) == 6


def test_part_2_debug():
    assert part_2(["L200"]) == 2
    assert part_2(["L250"]) == 3
    assert part_2(["R200"]) == 2
    assert part_2(["R250"]) == 3
