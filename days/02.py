from typing import Callable
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/02.actual")
example_input = parse_file("days/inputs/02.example")


def is_valid_id(id: str) -> bool:
    if len(id) % 2 == 1:
        return True
    middle = len(id) // 2
    return id[0:middle] != id[middle : len(id)]


def test_is_valid_id():
    assert not is_valid_id("11")
    assert is_valid_id("12")


def loop(id_range: str, is_valid_id_tester: Callable[[str], bool]) -> int:
    [begin, end] = map(int, id_range.split("-"))
    return sum(
        map(
            lambda x: x if not is_valid_id_tester(str(x)) else 0,
            range(begin, end + 1),
        )
    )


def part_1(lines: list[str]) -> int:
    ranges = lines[0].split(",")
    return sum(map(lambda x: loop(x, is_valid_id), ranges))


def test_part_1():
    assert part_1(actual_input) == 32976912643


def test_part_1_example():
    assert part_1(example_input) == 1227775554


def is_valid_id_part_2(id: str) -> bool:
    for n in range(int(len(id) / 2)):
        repeat_times = len(id) // (n + 1)
        repeat_section = id[0 : (n + 1)] * repeat_times
        if id == repeat_section:
            return False
    middle = int(len(id) / 2)
    return id[0:middle] != id[middle : len(id)]


def test_is_valid_id_part_2():
    assert not is_valid_id_part_2("11")
    assert is_valid_id_part_2("12")
    assert not is_valid_id_part_2("12341234")
    assert not is_valid_id_part_2("123123123")
    assert not is_valid_id_part_2("1212121212")
    assert not is_valid_id_part_2("1111111")


def part_2(lines: list[str]) -> int:
    ranges = lines[0].split(",")
    return sum(map(lambda x: loop(x, is_valid_id_part_2), ranges))


def test_part_2():
    assert part_2(actual_input) == 54446379122


def test_part_2_example():
    assert part_2(example_input) == 4174379265
