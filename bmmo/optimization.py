from bmmo.blocks_table import BlocksTable
from bmmo.block import Block

# The idea is to get the most top left block.
# We try to expand its width on its right as much as possible.
# Once it's not possible anymore, we expand its height on the bottom as much as possible while keeping the same width.
# When we cannot expand it anymore because the width is not maintained or the maximum height has been reached, we create
# a block with the new width and height.
# Now, we can remove the newly created block from the given table of blocks.
# Finally, we repeat the process.
def get_least_blocks_from_blocks_table(blocks_table: BlocksTable) -> list[Block]:
    blocks = [Block(0, 0, 1, 1, blocks_table.type, blocks_table.sound)]
    return blocks
