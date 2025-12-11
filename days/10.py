from utils.parse_file import parse_file

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


# # takes 633 seconds...
# def test_part_1_actual():
#     assert part_1(actual_input) == 522
