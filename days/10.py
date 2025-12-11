from typing import cast
from utils.parse_file import parse_file
from z3 import Int, Solver, Sum, sat, IntNumRef

actual_input = parse_file("days/inputs/10.actual")
example_input = parse_file("days/inputs/10.example")

type LightDiagram = list[bool]
type ButtonWirings = list[list[int]]
type JoltageRequirments = list[int]
type Machine = tuple[LightDiagram, ButtonWirings, JoltageRequirments]


def parse_input(
    lines: list[str],
) -> list[Machine]:
    result = []
    for line in lines:
        light_diagram_end = line.index("]")
        joltage_requirements_start = line.index("{")
        light_diagram = list(light == "#" for light in line[1:light_diagram_end])
        button_wirings = list(
            map(
                lambda x: list(map(int, x[1:-1].split(","))),
                line[light_diagram_end + 2 : joltage_requirements_start - 1].split(),
            )
        )
        joltage_requirements = list(
            map(int, line[joltage_requirements_start + 1 : -1].split(","))
        )
        result.append((light_diagram, button_wirings, joltage_requirements))
    return result


def find_button_presses(machine: Machine) -> int:
    target_light_diagram, button_wirings, joltage_requirements = machine
    light_diagram = [False] * len(target_light_diagram)
    queue = []
    queue.append((0, light_diagram))

    while len(queue) > 0:
        (presses, light_diagram) = queue.pop(0)
        if presses > 10:
            print(light_diagram)
            break
        if light_diagram == target_light_diagram:
            return presses
        for button_wiring in button_wirings:
            new_light_diagram = light_diagram.copy()
            for button in button_wiring:
                new_light_diagram[button] = not new_light_diagram[button]
            queue.append((presses + 1, new_light_diagram))
    return 0


def part_1(lines: list[str]) -> int:
    machines = parse_input(lines)
    return sum(map(find_button_presses, machines))


def test_part_1_example():
    assert part_1(example_input) == 7


# takes 633 seconds... beware
def test_part_1_actual():
    assert part_1(actual_input) == 522


# tried it like part 1 but was way too slow
# read that a lot of people tried things like A*, pruning, etc but still too slow or not guaranteed to find an answer
# so looked into z3 for a solution as I was not going to implement a MILP solver myself
def part_2(lines: list[str]) -> int:
    machines = parse_input(lines)
    total = 0
    for _, button_wirings, joltage_requirements in machines:
        solver = Solver()

        button_vars = [Int(f"a{n}") for n in range(len(button_wirings))]
        for var in button_vars:
            solver.add(var >= 0)

        for joltage_index, joltage_requirement in enumerate(joltage_requirements):
            joltage_vars = [
                button_vars[button_index]
                for button_index, button in enumerate(button_wirings)
                if joltage_index in button
            ]
            solver.add(Sum(joltage_vars) == joltage_requirement)

        machine_result = 0
        while solver.check() == sat:
            model = solver.model()
            machine_result = sum(
                [cast(IntNumRef, model[result]).as_long() for result in model]
            )
            solver.add(Sum(button_vars) < machine_result)

        total += machine_result
    return total


def test_part_2_example():
    assert part_2(example_input) == 33


def test_part_2_actual():
    assert part_2(actual_input) == 18105
