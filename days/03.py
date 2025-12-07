from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/03.actual")
example_input = parse_file("days/inputs/03.example")


# this was the naive solution
# def get_largest_joltage(bank: str, batteries: int) -> int:
#     return max(map(int, map(lambda x: x[0] + x[1], combinations(bank, batteries))))


def get_largest_joltage(bank: str, batteries_remaining: int) -> int:
    result, current_digit, position = 0, 0, -1
    while batteries_remaining > 0:
        # only select subsequent digits without going to far
        for pos in range(position + 1, len(bank) - batteries_remaining + 1):
            if int(bank[pos]) > current_digit:
                current_digit = int(bank[pos])
                position = pos
        batteries_remaining -= 1
        result *= 10
        result += current_digit
        current_digit = 0
    return result


def test_get_largest_joltage():
    assert get_largest_joltage("987654321111111", 2) == 98
    assert get_largest_joltage("811111111111119", 2) == 89
    assert get_largest_joltage("234234234234278", 2) == 78
    assert get_largest_joltage("818181911112111", 2) == 92


def part_1(lines: list[str]) -> int:
    return sum(map(lambda bank: get_largest_joltage(bank, 2), lines))


def test_part_1():
    assert part_1(actual_input) == 17524


def test_part_1_example():
    assert part_1(example_input) == 357


def part_2(lines: list[str]) -> int:
    return sum(map(lambda bank: get_largest_joltage(bank, 12), lines))


def test_part_2():
    assert part_2(actual_input) == 173848577117276


def test_part_2_example():
    assert part_2(example_input) == 3121910778619
