from bmmo.blocks_table import BlocksTable


def get_bmap_measures(bmap: dict) -> (int, int):
    """
    Given a bmap, get the width and height of the map
    :param bmap: The bmap
    :return: width, height
    """
    config = bmap['Config']
    return int(config['MapWidth']), int(config['MapHeight'])


def separate_objects_from_other_objects(bmap: dict, objs_to_separate_names: list[str]) -> (list[dict], list[dict]):
    """
    Given a bmap, separate the blocks/walls and all other objects
    :param bmap: The bmap
    :param objs_to_separate_names: List of names for the objects to search for
    :return: a list of blocks/walls, a list of all other objects
    """
    blocks_list = []
    others_list = []

    for key, obj in bmap.items():
        if (key != 'Config') and (obj['Name'] in objs_to_separate_names):
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


def _get_coordinates_and_sizes(
        block: dict,
        wall_name: str,
        blocks_info: dict[str, dict[str, int]]
) -> (int, int, int, int):
    x, y = block['X'], block['Y']
    if block['Name'] == wall_name:
        return int(x), int(y), int(block['ObjWallWidth']), int(block['ObjWallHeight'])

    block_info = blocks_info[block['Name']]
    return int(x), int(y), block_info['width'], block_info['height']


def from_blocks_to_list_of_blocks_table(
        map_width: int,
        map_height: int,
        blocks_list: list[dict],
        wall_name: str,
        blocks_info: dict[str, dict[str, int]],
        block_size: int = 1
) -> list[BlocksTable]:
    """
    Given a list of blocks, it returns a table of 0 and 1
    :param map_width: width of the map, blocks outside of the given width will not be in the table
    :param map_height: height of the map, blocks outside of the given height will not be in the table
    :param blocks_list: blocks to put in the table
    :param wall_name: name of the wall tool
    :param blocks_info: list of the different blocks information
    :param block_size: used to scale the sizes and coordinates, advised to use if blocks are snapped to the map grid
    :return: A list of BlocksTable. The table is composed of 0 & 1. 1 represents the presence of a block.
    """
    scaled_map_width = int(map_width / block_size)
    scaled_map_height = int(map_height / block_size)
    table = _create_table(scaled_map_width, scaled_map_height)

    list_of_blocks_table = [BlocksTable('0', '0', table)]

    def check_coordinates(x: int, y: int):
        return (0 <= x < scaled_map_width) and (0 <= y < scaled_map_height)

    def is_divisible(dividend: int, divisor: int) -> bool:
        return dividend % divisor == 0

    def update_blocks_table(x: int, y: int, w: int, h: int, blocks_table: BlocksTable):
        if not is_divisible(x, block_size) or not is_divisible(y, block_size):
            return

        scaled_w = int(w / block_size)
        scaled_h = int(h / block_size)
        scaled_x = int(x / block_size)
        scaled_y = int(y / block_size)

        for j in range(scaled_y, scaled_y + scaled_h):
            for i in range(scaled_x, scaled_x + scaled_w):
                if check_coordinates(i, j):
                    blocks_table[j][i] = 1

    for block in blocks_list:
        x, y, width, height = _get_coordinates_and_sizes(block, wall_name, blocks_info)
        update_blocks_table(x, y, width, height, list_of_blocks_table[0])

    return list_of_blocks_table
