from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/07.actual")
example_input = parse_file("days/inputs/07.example")


def parse_lines(lines: list[str]) -> tuple[tuple[int, int], list[list[int]]]:
    s_position = (lines[0].index("S"), 0)
    parsed_lines = list(
        list(map(lambda x: 0 if x == "." else -1, list(line))) for line in lines
    )
    return (s_position, parsed_lines)


def part_1(lines: list[str]) -> int:
    (start, parsed_lines) = parse_lines(lines)
    positions = list([start])
    times_split = 0
    for y in range(len(lines) - 1):
        for _ in range(len(positions)):
            (first_x, first_y) = positions.pop(0)
            new_y = first_y + 1
            if lines[new_y][first_x] == "^":
                times_split += 1
                if (first_x - 1, new_y) not in positions:
                    positions.append((first_x - 1, new_y))
                if (first_x + 1, new_y) not in positions:
                    positions.append((first_x + 1, new_y))
            else:
                if (first_x, new_y) not in positions:
                    positions.append((first_x, new_y))
    return times_split


def test_part_1_example():
    assert part_1(example_input) == 21


def test_part_1_actual():
    assert part_1(actual_input) == 1546


def part_2(lines: list[str]) -> int:
    (start, parsed_lines) = parse_lines(lines)
    # print(parsed_lines)
    positions = list([start])
    for y in range(len(lines) - 1):
        for _ in range(len(positions)):
            (first_x, first_y) = positions.pop(0)
            # print("setting", first_x, first_y)
            parsed_lines[first_y][first_x] += 1
            new_y = first_y + 1
            if parsed_lines[new_y][first_x] == -1:
                # print('splitter found')
                # if (first_x - 1, new_y) not in positions:
                positions.append((first_x - 1, new_y))
                # if (first_x + 1, new_y) not in positions:
                positions.append((first_x + 1, new_y))
            else:
                # if (first_x, new_y) not in positions:
                positions.append((first_x, new_y))
    # last line was not used in parsed_lines so we take second to last line
    return sum(list(map(lambda x: 0 if x == -1 else x, parsed_lines[-2])))


def test_part_2_example():
    assert part_2(example_input) == 40


def test_part_2_actual():
    assert part_2(actual_input) == 3131  # too low
