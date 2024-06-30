def get_lines(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = [line.rstrip() for line in file]
    return lines
