from collections import namedtuple
from functools import cache
from utils.parse_file import parse_file

actual_input = parse_file("days/inputs/11.actual")
part_1_example_input = parse_file("days/inputs/11.part1.example")
part_2_example_input = parse_file("days/inputs/11.part2.example")


def parse_input(lines: list[str]) -> dict:
    graph = {}
    for line in lines:
        (origin, targets) = line.split(": ")
        graph[origin] = list(targets.split())
    graph["out"] = []
    return graph


def part_1(lines: list[str]) -> int:
    QueueItem = namedtuple("QueueItem", ["target", "visited"])
    graph = parse_input(lines)
    queue = [QueueItem("you", [])]
    paths_found = []
    while len(queue) > 0:
        (target, visited) = queue.pop(0)
        for new_target in graph[target]:
            if new_target == "out":
                paths_found.append(visited)
            elif new_target not in visited:
                queue.append(QueueItem(new_target, visited + [new_target]))
    return len(paths_found)


def test_part_1_example():
    assert part_1(part_1_example_input) == 5


def test_part_1_actual():
    assert part_1(actual_input) == 466


def part_2(lines: list[str]) -> int:
    graph = parse_input(lines)

    @cache
    def search_path(origin, target):
        if target in graph[origin]:
            return 1
        return (target in graph[origin]) + sum(
            search_path(node, target) for node in graph[origin]
        )

    return search_path("svr", "fft") * search_path("fft", "dac") * search_path(
        "dac", "out"
    ) + search_path("svr", "dac") * search_path("dac", "fft") * search_path(
        "fft", "out"
    )


def test_part_2_example():
    assert part_2(part_2_example_input) == 2


def test_part_2_actual():
    assert part_2(actual_input) == 549705036748518
