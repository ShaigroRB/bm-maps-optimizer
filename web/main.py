from browser import document

def hello():
    document <= "Hello !"


# import sys
# import json
# from bmmo.constants import MAP_OBJECTS_INDEX, BLOCK_SIZE, BLOCKS_AND_WALL_NAMES, WALL_TOOL, BLOCKS
# from bmmo.parsing import get_bmap_measures, separate_objects_from_other_objects, from_blocks_to_list_of_blocks_table


# def get_lines(filepath: str) -> list[str]:
#     with open(filepath, 'r') as file:
#         lines = [line.rstrip() for line in file]
#     return lines


# def string_to_json(string: str) -> dict:
#     _json = json.loads(string)
#     return _json


# def print_table(table: list[list[int]]):
#     for row in table:
#         print(row)


# def optimize_table(table: list[list[int]]) -> list[Block]:
#     pass


# if __name__ == '__main__':
#     path = sys.argv[1]
#     original_lines = get_lines(path)
#     bmap_json = string_to_json(original_lines[MAP_OBJECTS_INDEX])
#     _map_width, _map_height = get_bmap_measures(bmap_json)
#     blocks_to_optimize, objects_to_keep = separate_objects_from_other_objects(bmap_json, BLOCKS_AND_WALL_NAMES)
#     list_of_blocks_table = from_blocks_to_list_of_blocks_table(
#         _map_width, _map_height,
#         blocks_to_optimize,
#         WALL_TOOL, BLOCKS, BLOCK_SIZE
#     )
#     print_table(list_of_blocks_table[0].table)
