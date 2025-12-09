from collections import defaultdict
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/07.actual")
example_input = parse_file("days/inputs/07.example")


def part_1(lines: list[str]) -> int:
    start = (lines[0].index("S"), int(0))
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
    start_x = lines[0].index("S")
    beams = {start_x: 1}
    for line in lines:
        new_beams = defaultdict(int)
        for i, n in beams.items():
            if line[i] == "^":
                new_beams[i - 1] += n
                new_beams[i + 1] += n
            else:
                new_beams[i] += n
        beams = new_beams
    return sum(beams[index] for index in beams)


def test_part_2_example():
    assert part_2(example_input) == 40


def test_part_2_actual():
    assert part_2(actual_input) == 13883459503480
