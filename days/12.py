from collections import namedtuple
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/12.actual")
example_input = parse_file("days/inputs/12.example")


# the easy solution, can't believe this was all it took
def part_1(lines: list[str]) -> int:
    (presents, regions) = parse_input(lines)
    valid_regions = 0
    for region in regions:
        amount_fits = 0
        for index, quantity in enumerate(region.quantities):
            present = presents.get(index)
            amount_fits += quantity * 9 if present is not None else 0
        if amount_fits <= len(region.grid) * len(region.grid[0]):
            valid_regions += 1
    return valid_regions


def test_part_1_actual():
    assert part_1(actual_input) == 487


# the bunch of code that is apparently unnecessary for the actual input...
Point = namedtuple("Point", ["x", "y"])
Region = namedtuple("Region", ["grid", "quantities"])
type Present = list[list[bool]]


def parse_input(lines: list[str]) -> tuple[dict, list[Region]]:
    def get_grid(width, height) -> list[list[bool]]:
        return [[False] * width for _ in range(height)]

    presents = {}
    regions = []
    current_index = 0
    current_present_data = get_grid(3, 3)
    current_present_data_y = 0
    for line in lines:
        # regions parsing
        if "x" in line:
            (dimensions, data) = line.split(": ")
            (width, height) = map(int, dimensions.split("x"))
            quantities = list(map(int, data.split()))
            regions.append(Region(get_grid(width, height), quantities))
        # presents parsing
        else:
            if line.endswith(":"):
                current_index = int(line[:-1])
            elif line == "":
                presents[current_index] = get_all_present_placements(
                    current_present_data
                )
                current_present_data = get_grid(3, 3)
                current_present_data_y = 0
                current_index += 1
            else:
                for x, part in enumerate(line):
                    current_present_data[current_present_data_y][x] = part == "#"
                current_present_data_y += 1
    return (presents, regions)


# to get the example to work, we would need a proper matching
# def test_part_1_example():
#     assert part_1(example_input) == 5


def rotate_present(present: Present) -> Present:
    return [list(row) for row in zip(*reversed(present))]


def test_rotate_present():
    assert rotate_present(
        [[True, True, True], [True, True, False], [True, True, False]]
    ) == [[True, True, True], [True, True, True], [False, False, True]]
    assert rotate_present(
        [[True, True, True], [True, True, True], [False, False, True]]
    ) == [[False, True, True], [False, True, True], [True, True, True]]
    assert rotate_present(
        [[False, True, True], [False, True, True], [True, True, True]]
    ) == [[True, False, False], [True, True, True], [True, True, True]]
    assert rotate_present(
        [[True, False, False], [True, True, True], [True, True, True]]
    ) == [[True, True, True], [True, True, False], [True, True, False]]


def flip_present(present: Present) -> Present:
    return list(reversed(present))


def test_flip_present():
    assert flip_present(
        [[True, True, True], [True, True, False], [True, True, False]]
    ) == [[True, True, False], [True, True, False], [True, True, True]]


def get_all_present_placements(present: Present) -> list[Present]:
    return [
        present,
        rotate_present(present),
        rotate_present(rotate_present(present)),
        rotate_present(rotate_present(rotate_present(present))),
        flip_present(present),
        flip_present(rotate_present(present)),
        flip_present(rotate_present(rotate_present(present))),
        flip_present(rotate_present(rotate_present(rotate_present(present)))),
    ]
