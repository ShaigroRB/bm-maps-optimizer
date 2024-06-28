import sys
import json
from bmmo.constants import MAP_OBJECTS_INDEX, BLOCK_SIZE, BLOCKS_AND_WALL_NAMES, WALL_TOOL, BLOCKS
from bmmo.parsing import get_bmap_measures, separate_objects_from_other_objects, from_blocks_to_list_of_blocks_table
from bmmo.optimization import get_least_blocks_from_blocks_table
from bmmo.block import Block


def string_to_json(string: str) -> dict:
    _json = json.loads(string)
    return _json


def print_table(table: list[list[int]]):
    for row in table:
        print(row)


def merge_map_objects_to_string(blocks: list[Block], scale: int, others: list) -> str:
    final_string = ""
    bmap = {}

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

    has_crashed = False
    try:
        final_string = json.dumps(bmap)
    except:
        has_crashed = True
        print('fail to serialize via "json.dumps"')

    if not has_crashed:
        return final_string, has_crashed
    else:
        return bmap, has_crashed


def optimize(og_lines: list[str]):
    """Takes a list of lines that represents a bmap.txt.
    Returns a list of lines that represents the newly optimized bmap.txt
    """
    # parse the file
    original_lines = og_lines
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
    compression_ratio = int((1 - (len_optimized / len_original)) * 100)
    print(f"Before: {len_original}, After: {len_optimized}")
    print(f"Compression ratio: {compression_ratio}%")
    if not (len_optimized < len_original):
        print("No optimization to be made")
        return

    # create a list of lines representing a new optimized bmap.txt
    optimized_objects_string, has_crashed = merge_map_objects_to_string(list_of_blocks, BLOCK_SIZE, objects_to_keep)

    stats = {
        "before": len_original,
        "after": len_optimized,
        "ratio": compression_ratio,
        "has_crashed": has_crashed,
    }

    optimized_lines = []
    for line in original_lines[0:MAP_OBJECTS_INDEX]:
        optimized_lines.append(line)
    optimized_lines.append(optimized_objects_string)
    optimized_lines.append(original_lines[MAP_OBJECTS_INDEX + 1])
    return optimized_lines, stats
