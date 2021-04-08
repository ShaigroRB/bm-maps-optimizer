from bmmo.constants import WALL_TOOL, BLOCKS


def get_bmap_measures(bmap: dict) -> (int, int):
    config = bmap['Config']
    return int(config['MapWidth']), int(config['MapHeight'])


def get_blocks_and_others(bmap: dict) -> (list[dict], list[dict]):
    blocks_list = []
    others_list = []

    for key, obj in bmap.items():
        if (key != 'Config') \
                and ((obj['Name'] in BLOCKS) or (obj['Name'] == WALL_TOOL)):
            blocks_list.append(obj)
        else:
            others_list.append(obj)

    return blocks_list, others_list


def _create_table(width: int, height: int) -> list[list[int]]:
    row = [0] * width
    columns = []
    for col in range(height):
        columns.append(list(row))
    return columns


def _get_coordinates_and_sizes(block: dict) -> (int, int, int, int):
    x, y = block['X'], block['Y']
    if block['Name'] == WALL_TOOL:
        return int(x), int(y), int(block['ObjWallWidth']), int(block['ObjWallHeight'])

    block_info = BLOCKS[block['Name']]
    return int(x), int(y), block_info['width'], block_info['height']


def from_blocks_to_table(map_width: int, map_height: int, blocks_list: list[dict], block_size: int = 1) \
        -> list[list[int]]:
    """
    Given a list of blocks, it returns a table of 0 and 1
    :param map_width: width of the map, blocks outside of the given width will not be in the table
    :param map_height: height of the map, blocks outside of the given height will not be in the table
    :param blocks_list: blocks to put in the table
    :param block_size: used to scale the sizes and coordinates, advised to use if blocks are snapped to the map grid
    :return: A table of 0 and 1. 1 means the presence of a block.
    """
    scaled_map_width = int(map_width / block_size)
    scaled_map_height = int(map_height / block_size)
    table = _create_table(scaled_map_width, scaled_map_height)

    def check_coordinates(x: int, y: int):
        return (0 <= x < scaled_map_width) and (0 <= y < scaled_map_height)

    def is_divisible(dividend: int, divisor: int) -> bool:
        return dividend % divisor == 0

    def update_table(x: int, y: int, w: int, h: int):
        if not is_divisible(x, block_size) or not is_divisible(y, block_size):
            return

        scaled_w = int(w / block_size)
        scaled_h = int(h / block_size)
        scaled_x = int(x / block_size)
        scaled_y = int(y / block_size)

        for j in range(scaled_y, scaled_y + scaled_h):
            for i in range(scaled_x, scaled_x + scaled_w):
                if check_coordinates(i, j):
                    table[j][i] = 1

    for block in blocks_list:
        x, y, width, height = _get_coordinates_and_sizes(block)
        update_table(x, y, width, height)

    return table
