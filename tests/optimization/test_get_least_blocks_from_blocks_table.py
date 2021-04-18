from bmmo.optimization import get_least_blocks_from_blocks_table
from bmmo.blocks_table import BlocksTable
from bmmo.block import Block


# when it is written table instead of blocks table,
# this mean we are testing the table result only and we don't care about block types nor blocks sounds
def test_table_is_1x1_full_of_1_should_return_list_of_length_1():
    blocks_table = BlocksTable('', '', [[1]])

    list_of_blocks = get_least_blocks_from_blocks_table(blocks_table)

    assert len(list_of_blocks) == 1


def test_table_is_1x1_full_of_1_type_sound_0_should_return_block_type_sound_0():
    blocks_table = BlocksTable('0', '0', [[1]])

    blocks = get_least_blocks_from_blocks_table(blocks_table)

    assert blocks[0].type == '0'
    assert blocks[0].sound == '0'


def test_table_is_1x1_full_of_1_type_2_sound_1_should_return_block_type_2_sound_1():
    blocks_table = BlocksTable('2', '1', [[1]])

    blocks = get_least_blocks_from_blocks_table(blocks_table)

    assert blocks[0].type == '2'
    assert blocks[0].sound == '1'


def test_table_is_1x1_full_of_1_should_return_block_x_y_0_width_height_1():
    blocks_table = BlocksTable('', '', [[1]])
    expected_block = Block(0, 0, 1, 1, '', '')

    list_of_blocks = get_least_blocks_from_blocks_table(blocks_table)
    block = list_of_blocks[0]

    assert block.x == expected_block.x
    assert block.y == expected_block.y
    assert block.width == expected_block.width
    assert block.height == expected_block.height


def test_table_is_2x2_second_row_full_of_1_should_return_block_x_0_y_1_width_2_height_1():
    blocks_table = BlocksTable('0', '0', [
        [0, 0],
        [1, 1]
    ])

    blocks = get_least_blocks_from_blocks_table(blocks_table)
    block = blocks[0]

    assert block.x == 0
    assert block.y == 1
    assert block.width == 2
    assert block.height == 1


def test_table_is_4x4_continuous_row_of_1_should_return_list_of_length_3():
    blocks_table = BlocksTable('0', '0', [
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
    ])

    blocks = get_least_blocks_from_blocks_table(blocks_table)

    assert len(blocks) == 3


def test_table_is_4x4_continuous_row_of_1_should_return_3_blocks_of_different_coordinates_and_sizes():
    blocks_table = BlocksTable('0', '0', [
        [1, 1, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 1, 1]
    ])

    blocks = get_least_blocks_from_blocks_table(blocks_table)
    block1 = blocks[0]
    block2 = blocks[1]
    block3 = blocks[2]

    assert block1.x == 0
    assert block1.y == 0
    assert block1.width == 3
    assert block1.height == 2

    assert block2.x == 2
    assert block2.y == 2
    assert block2.width == 2
    assert block2.height == 2

    assert block3.x == 0
    assert block3.y == 3
    assert block3.width == 2
    assert block3.height == 1
