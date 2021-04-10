from bmmo.parsing import from_blocks_to_list_of_blocks_table
from bmmo.constants import BLOCKS, WALL_TOOL

list_of_128_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def test_default_1x1_map_width_height_of_128_should_return_blocks_table_of_128x128():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]
    # default block size: 128 * 128
    expected_table = [list(list_of_128_1) for _ in range(128)]

    blocks_tables = from_blocks_to_list_of_blocks_table(128, 128, blocks, 'Wall Tool', BLOCKS)

    assert len(blocks_tables[0].table) == len(expected_table)
    assert len(blocks_tables[0].table[0]) == len(expected_table[0])


def test_default_1x1_map_width_height_of_128_should_return_blocks_table_full_of_1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]
    # default block size: 128 * 128
    expected_table = [list(list_of_128_1) for _ in range(128)]

    blocks_tables = from_blocks_to_list_of_blocks_table(128, 128, blocks, WALL_TOOL, BLOCKS)

    assert blocks_tables[0].table == expected_table


def test_no_block_should_return_empty_list():
    blocks = []

    blocks_table = from_blocks_to_list_of_blocks_table(0, 0, blocks, WALL_TOOL, BLOCKS)

    assert len(blocks_table) == 0
