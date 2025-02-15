// a map file is composed of name, is the map a climb map, steam workshop id, objects, tiles hashes
export const MAP_OBJECTS_INDEX = 3;
export const BLOCK_SIZE = 128;

export const BLOCKS = {
  "Block (1x1)": {
    id: 0,
    width: 1 * BLOCK_SIZE,
    height: 1 * BLOCK_SIZE,
  },
  "Block (2x2)": {
    id: 63,
    width: 2 * BLOCK_SIZE,
    height: 2 * BLOCK_SIZE,
  },
  "Block (1x4)": {
    id: 43,
    width: 1 * BLOCK_SIZE,
    height: 4 * BLOCK_SIZE,
  },
  "Block (4x1)": {
    id: 42,
    width: 4 * BLOCK_SIZE,
    height: 1 * BLOCK_SIZE,
  },
};

export const WALL_TOOL = "Wall Tool";

export const BLOCKS_AND_WALL_NAMES = [
  "Block (1x1)",
  "Block (2x2)",
  "Block (1x4)",
  "Block (4x1)",
  "Wall Tool",
];
