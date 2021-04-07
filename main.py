import sys
import json
from constants import MAP_OBJECTS_INDEX, BLOCK_SIZE
from parsing import get_bmap_measures, get_blocks_and_others, from_blocks_to_table


def get_lines(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        lines = [line.rstrip() for line in file]
    return lines


def string_to_json(string: str) -> dict:
    _json = json.loads(string)
    return _json


def print_table(table: list[list[int]]):
    for row in table:
        print(row)


if __name__ == '__main__':
    path = sys.argv[1]
    original_lines = get_lines(path)
    bmap_json = string_to_json(original_lines[MAP_OBJECTS_INDEX])
    _map_width, _map_height = get_bmap_measures(bmap_json)
    blocks_to_optimize, objects_to_keep = get_blocks_and_others(bmap_json)
    table = from_blocks_to_table(_map_width, _map_height, blocks_to_optimize, BLOCK_SIZE)
    print_table(table)
