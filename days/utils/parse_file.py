def parse_file(filename: str) -> list[str]:
    with open(filename) as f:
        input_data = f.read()
    return input_data.strip().splitlines()