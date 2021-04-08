# a map file is composed of name, ?, ?, objects, tiles hashes
MAP_OBJECTS_INDEX = 3
BLOCK_SIZE = 128
BLOCKS = {
    'Block (1x1)': {
        'id': 0,
        'width': 1 * BLOCK_SIZE,
        'height': 1 * BLOCK_SIZE
    },
    'Block (2x2)': {
        'id': 63,
        'width': 2 * BLOCK_SIZE,
        'height': 2 * BLOCK_SIZE
    },
    'Block (1x4)': {
        'id': 43,
        'width': 1 * BLOCK_SIZE,
        'height': 4 * BLOCK_SIZE
    },
    'Block (4x1)': {
        'id': 42,
        'width': 4 * BLOCK_SIZE,
        'height': 1 * BLOCK_SIZE
    }
}
WALL_TOOL = 'Wall Tool'
