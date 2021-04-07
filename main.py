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


def get_bmap_measures(bmap: dict) -> (int, int):
    config = bmap['Config']
    return int(config['MapWidth']), int(config['MapHeight'])
if __name__ == '__main__':
    path = sys.argv[1]
    original_lines = get_lines(path)
    bmap_json = string_to_json(original_lines[MAP_OBJECTS_INDEX])
    _map_width, _map_height = get_bmap_measures(bmap_json)
