def parse_file(filename: str) -> list[str]:
    with open(filename) as f:
        input_data = f.read()
    return input_data.strip().splitlines()


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
        position = position % (-100 if position < 0 else 100)
        if position == 0:
            times_0 += 1
    return times_0


def test_part_1():
    assert part_1(parse_file("days/01.actual")) == 1139


def test_part_1_example():
    assert part_1(parse_file("days/01.example")) == 3
