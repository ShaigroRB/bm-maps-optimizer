import sys


def get_lines(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = [line.rstrip() for line in file]
    return lines
if __name__ == '__main__':
    path = sys.argv[1]
    original_lines = get_lines(path)
