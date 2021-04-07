import sys
import json
from constants import MAP_OBJECTS_INDEX, BLOCK_SIZE, BLOCKS, WALL_TOOL


def get_lines(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = [line.rstrip() for line in file]
    return lines


def string_to_json(string: str) -> dict:
    _json = json.loads(string)
    return _json
if __name__ == '__main__':
    path = sys.argv[1]
    original_lines = get_lines(path)
    bmap_json = string_to_json(original_lines[MAP_OBJECTS_INDEX])
