import sys
import json
from bmmo.constants import MAP_OBJECTS_INDEX, BLOCK_SIZE, BLOCKS_AND_WALL_NAMES, WALL_TOOL, BLOCKS
from bmmo.parsing import get_bmap_measures, separate_objects_from_other_objects, from_blocks_to_list_of_blocks_table
from bmmo.optimization import get_least_blocks_from_blocks_table
from bmmo.block import Block
from bmmo.file import get_lines


def string_to_json(string: str) -> dict:
    _json = json.loads(string)
    return _json


def print_table(table: list[list[int]]):
    for row in table:
        print(row)


def merge_map_objects_to_string(blocks: list[Block], scale: int, others: list) -> str:
    final_string = ""
    bmap = {
    }

    last_index = len(others)

    def create_object_from_block(block: Block, id: int) -> dict:
        return {
            "X": str(block.x * scale),
            "Y": str(block.y * scale),
            "ObjWallWidth": str(block.width * scale),
            "ObjWallHeight": str(block.height * scale),
            "ID": str(id),
            "ObjIndexID": "46",
            "Name": "Wall Tool",
            "LogidID": str(id),
            "Poly": "0",
            "ObjIsTile": "0",
            "Depth": "500",
            "ObjType": block.type,
            "ObjSound": block.sound,
            "Team": "-1",
        }

    for index, obj in enumerate(others):
        if 'Author' in obj:
            bmap["Config"] = obj
        else:
            bmap[f"OBJ{index}"] = obj

    for index, block in enumerate(blocks):
        block_id = last_index + index
        bmap[f"OBJ{block_id}"] = create_object_from_block(block, block_id)

    final_string = json.dumps(bmap)
    return final_string


def main(path: str):
    # parse the file
    original_lines = get_lines(path)
    bmap_json = string_to_json(original_lines[MAP_OBJECTS_INDEX])
    _map_width, _map_height = get_bmap_measures(bmap_json)

    # put the blocks and walls in a single list
    blocks_to_optimize, objects_to_keep = separate_objects_from_other_objects(bmap_json, BLOCKS_AND_WALL_NAMES)

    # create blocks table from blocks/walls objects of the map
    list_of_blocks_table = from_blocks_to_list_of_blocks_table(
        _map_width, _map_height,
        blocks_to_optimize,
        WALL_TOOL, BLOCKS, BLOCK_SIZE
    )

    list_of_blocks = []

    # optimize the blocks
    for blocks_table in list_of_blocks_table:
        curr_blocks = get_least_blocks_from_blocks_table(blocks_table)
        list_of_blocks = [*list_of_blocks, *curr_blocks]

    # log some information about the optimization
    len_original = len(blocks_to_optimize)
    len_optimized = len(list_of_blocks)
    print(f"Before: {len_original}, After: {len_optimized}")
    print(f"Compression ratio: {int((1 - (len_optimized / len_original)) * 100)}%")
    if not (len_optimized < len_original):
        return

    # create an optimized bmap file
    optimized_objects_string = merge_map_objects_to_string(list_of_blocks, BLOCK_SIZE, objects_to_keep)

    optimized_bmap_file = open('optimized_bmap.txt', 'w+')
    for line in original_lines[0:MAP_OBJECTS_INDEX]:
        optimized_bmap_file.write(line + '\n')
    optimized_bmap_file.write(optimized_objects_string + '\n')
    optimized_bmap_file.write(original_lines[MAP_OBJECTS_INDEX + 1] + '\n')

    optimized_bmap_file.close()


if __name__ == '__main__':
    path = sys.argv[1]
    main(path)
