from bmmo.blocks_table import BlocksTable
from bmmo.block import Block


def get_least_blocks_from_blocks_table(blocks_table: BlocksTable) -> list[Block]:
    blocks = [Block(0, 0, 1, 1, blocks_table.type, blocks_table.sound)]
    return blocks
