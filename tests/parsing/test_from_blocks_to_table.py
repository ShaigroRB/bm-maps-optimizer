from bmmo.parsing import from_blocks_to_list_of_blocks_table
from bmmo.constants import BLOCKS, WALL_TOOL


def test_default_1x1_map_width_height_of_128_should_return_table_of_128x128():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]
    # default block size: 128 * 128
    list_of_128_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_table = [list(list_of_128_1) for _ in range(128)]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(128, 128, blocks, WALL_TOOL, BLOCKS)

    assert len(list_of_blocks_table[0].table) == len(expected_table)
    assert len(list_of_blocks_table[0].table[0]) == len(expected_table[0])


def test_default_1x1_map_width_height_of_128_should_return_table_full_of_1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]
    # default block size: 128 * 128
    list_of_128_1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                     1,
                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    expected_table = [list(list_of_128_1) for _ in range(128)]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(128, 128, blocks, WALL_TOOL, BLOCKS)

    assert list_of_blocks_table[0].table == expected_table


def test_no_block_should_return_empty_list():
    blocks = []

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(0, 0, blocks, WALL_TOOL, BLOCKS)

    assert len(list_of_blocks_table) == 0


def test_default_1x1_map_width_height_of_128_with_scale_of_128_should_return_table_of_1x1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    expected_table = [[1]]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(128, 128, blocks, WALL_TOOL, BLOCKS, 128)

    assert len(list_of_blocks_table[0].table) == len(expected_table)


def test_default_1x1_map_width_height_of_128_with_scale_of_128_should_return_table_of_1x1_full_of_1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    expected_table = [[1]]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(128, 128, blocks, WALL_TOOL, BLOCKS, 128)

    assert list_of_blocks_table[0].table == expected_table


def test_two_blocks_with_similar_types_width_height_256_with_scale_of_128_should_return_blocks_table_list_of_length_1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
        {"Y": "128", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(256, 256, blocks, WALL_TOOL, BLOCKS, 128)

    assert len(list_of_blocks_table) == 1


def test_two_blocks_with_similar_types_width_height_256_with_scale_of_128_should_return_table_of_2x2_with_first_column_full_of_1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
        {"Y": "128", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    expected_table = [
        [1, 0],
        [1, 0]
    ]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(256, 256, blocks, WALL_TOOL, BLOCKS, 128)

    assert list_of_blocks_table[0].table == expected_table


def test_two_blocks_with_different_types_width_height_256_with_scale_of_128_should_return_blocks_table_list_of_length_2():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
        {"Y": "128", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "2", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(256, 256, blocks, WALL_TOOL, BLOCKS, 128)

    assert len(list_of_blocks_table) == 2


def test_two_blocks_with_different_types_width_height_256_with_scale_of_128_should_return_table_with_top_left_1_and_table_with_bottom_left_1():
    blocks = [
        {"Y": "0", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"},
        {"Y": "128", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "2", "X": "0",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    first_expected_table = [
        [1, 0],
        [0, 0]
    ]

    second_expected_table = [
        [0, 0],
        [1, 0]
    ]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(256, 256, blocks, WALL_TOOL, BLOCKS, 128)

    assert list_of_blocks_table[0].table == first_expected_table
    assert list_of_blocks_table[1].table == second_expected_table


def test_block_coordinates_256_256_width_height_128_should_return_empty_list():
    blocks = [
        {"Y": "256", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "256",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(128, 128, blocks, WALL_TOOL, BLOCKS)

    assert len(list_of_blocks_table) == 0


def test_block_coordinates_255_255_width_height_256_scale_128_should_return_empty_list():
    blocks = [
        {"Y": "255", "LogicID": "3", "Poly": "0", "ObjIsTile": "0", "Depth": "500", "ObjType": "0", "X": "255",
         "ObjSound": "0", "ID": "4", "Name": "Block (1x1)", "Team": "-1", "ObjIndexID": "0"}
    ]

    list_of_blocks_table = from_blocks_to_list_of_blocks_table(256, 256, blocks, WALL_TOOL, BLOCKS, 128)

    assert len(list_of_blocks_table) == 0
