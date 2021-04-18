from bmmo.blocks_table import BlocksTable
from bmmo.block import Block
import copy


def _is_cell_valid(cell: int) -> bool:
    return cell == 1


def _find_coordinates_of_most_top_left_valid_cell(table: list[list[int]]) -> (int, int):
    for j, row in enumerate(table):
        for i, column in enumerate(row):
            if _is_cell_valid(column):
                return i, j
    return -1, -1


def _is_row_start_to_end_valid(table: list[list[int]], row_index: int, start_index: int, end_index: int) -> bool:
    is_row_valid = True
    for i in range(start_index, end_index):
        is_row_valid = _is_cell_valid(table[row_index][i])
        if not is_row_valid:
            break
    return is_row_valid


def _remove_block_from_table(block: Block, table: list[list[int]]):
    for j in range(block.y, block.height + block.y):
        for i in range(block.x, block.width + block.x):
            table[j][i] = 0


# The idea is to get the most top left block.
# We try to expand its width on its right as much as possible.
# Once it's not possible anymore, we expand its height on the bottom as much as possible while keeping the same width.
# When we cannot expand it anymore because the width is not maintained or the maximum height has been reached, we create
# a block with the new width and height.
# Now, we can remove the newly created block from the given table of blocks.
# Finally, we repeat the process.
# Technically speaking, it doesn't get the least blocks possible. But in our use case, it's good enough.
def get_least_blocks_from_blocks_table(blocks_table: BlocksTable) -> list[Block]:
    """
    Get least blocks from a BlocksTable.
    :param blocks_table: a BlocksTable
    :return: a list of Block
    """

    block_type = blocks_table.type
    block_sound = blocks_table.sound
    nb_rows = len(blocks_table.table)
    nb_columns = len(blocks_table.table[0])
    blocks = []

    optimized_table = copy.deepcopy(blocks_table.table)

    def create_block(x: int, y: int, w: int, h: int) -> Block:
        return Block(x, y, w, h, block_type, block_sound)

    # for a more modular algorithm, add the find coordinates as a function given as parameter
    top_left_cell_x, top_left_cell_y = _find_coordinates_of_most_top_left_valid_cell(optimized_table)
    index_row, index_col = top_left_cell_y, top_left_cell_x + 1

    while (top_left_cell_x != -1) and (top_left_cell_y != -1):
        current_cell_is_valid = True

        # get the index of the first invalid cell from left to right
        # last valid index is: (invalid_index - 1)
        while (index_col < nb_columns) and current_cell_is_valid:
            current_cell = optimized_table[index_row][index_col]
            current_cell_is_valid = _is_cell_valid(current_cell)
            if current_cell_is_valid:
                index_col += 1

        index_invalid_cell = index_col
        index_row += 1
        current_row_is_valid = True

        # get the index of the first invalid row (top to bottom)
        while (index_row < nb_rows) and current_row_is_valid:
            current_row_is_valid = _is_row_start_to_end_valid(
                optimized_table,
                index_row, top_left_cell_x, index_invalid_cell
            )
            if current_row_is_valid:
                index_row += 1

        index_invalid_row = index_row

        block_width = index_invalid_cell - top_left_cell_x
        block_height = index_invalid_row - top_left_cell_y
        block = create_block(top_left_cell_x, top_left_cell_y, block_width, block_height)

        blocks.append(block)
        _remove_block_from_table(block, optimized_table)

        top_left_cell_x, top_left_cell_y = _find_coordinates_of_most_top_left_valid_cell(optimized_table)
        index_row, index_col = top_left_cell_y, top_left_cell_x + 1

    return blocks
