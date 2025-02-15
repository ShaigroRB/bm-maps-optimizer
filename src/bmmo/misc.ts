import {
  MAP_OBJECTS_INDEX,
  BLOCK_SIZE,
  BLOCKS_AND_WALL_NAMES,
  WALL_TOOL,
  BLOCKS,
} from "./constants";
import {
  getBmapMeasures,
  separateObjectsFromOtherObjects,
  fromBlocksToListOfBlocksTable,
} from "./parsing";
import { getLeastBlocksFromBlocksTable } from "./optimization";
import { Block } from "./block";

function stringToJson(str: string): Record<string, any> {
  return JSON.parse(str);
}

function printTable(table: number[][]): void {
  table.forEach((row) => console.log(row.join(" "), "\n"));
}

/**
 * Merges blocks and other map objects into a JSON string.
 * @param {Block[]} blocks - List of blocks to merge.
 * @param {number} scale - Scale to apply to block coordinates and dimensions.
 * @param {any[]} others - List of other map objects to include.
 * @returns {[string, boolean]} The resulting JSON string and a crash flag.
 */
export function mergeMapObjectsToString(
  blocks: Block[],
  scale: number,
  others: any[]
): [string, boolean] {
  const bmap: Record<string, any> = {};
  let hasCrashed = false;

  const createObjectFromBlock = (
    block: Block,
    id: number
  ): Record<string, string> => ({
    X: (block.x * scale).toString(),
    Y: (block.y * scale).toString(),
    ObjWallWidth: (block.width * scale).toString(),
    ObjWallHeight: (block.height * scale).toString(),
    ID: id.toString(),
    ObjIndexID: "46",
    Name: "Wall Tool",
    LogidID: id.toString(),
    Poly: "0",
    ObjIsTile: "0",
    Depth: "500",
    ObjType: block.type,
    ObjSound: block.sound,
    Team: "-1",
  });

  others.forEach((obj, index) => {
    if ("Author" in obj) {
      bmap["Config"] = obj;
    } else {
      bmap[`OBJ${index}`] = obj;
    }
  });

  blocks.forEach((block, index) => {
    const blockId = others.length + index;
    bmap[`OBJ${blockId}`] = createObjectFromBlock(block, blockId);
  });

  let finalString = "";
  try {
    finalString = JSON.stringify(bmap);
  } catch {
    hasCrashed = true;
    console.error('Failed to serialize via "JSON.stringify"');
  }

  return hasCrashed
    ? [JSON.stringify(bmap), hasCrashed]
    : [finalString, hasCrashed];
}

/**
 * Optimizes a map represented as lines of a bmap.txt file.
 * @param {string[]} ogLines - The original lines that represents a bmap.txt.
 * @returns {[string[], Record<string, number | boolean>]} The optimized lines and statistics.
 */
export function optimize(
  ogLines: string[]
): [string[], Record<string, number | boolean>] {
  const originalLines = ogLines;
  const bmapJson = stringToJson(originalLines[MAP_OBJECTS_INDEX]);
  const [_mapWidth, _mapHeight] = getBmapMeasures(bmapJson);

  const [blocksToOptimize, objectsToKeep] = separateObjectsFromOtherObjects(
    bmapJson,
    BLOCKS_AND_WALL_NAMES
  );

  const listOfBlocksTable = fromBlocksToListOfBlocksTable(
    _mapWidth,
    _mapHeight,
    blocksToOptimize,
    WALL_TOOL,
    BLOCKS,
    BLOCK_SIZE
  );

  let listOfBlocks: Block[] = [];

  listOfBlocksTable.forEach((blocksTable) => {
    const currBlocks = getLeastBlocksFromBlocksTable(blocksTable);
    listOfBlocks = [...listOfBlocks, ...currBlocks];
  });

  const lenOriginal = blocksToOptimize.length;
  const lenOptimized = listOfBlocks.length;
  const compressionRatio = Math.floor((1 - lenOptimized / lenOriginal) * 100);

  console.log(`Before: ${lenOriginal}, After: ${lenOptimized}`);
  console.log(`Compression ratio: ${compressionRatio}%`);

  if (lenOptimized >= lenOriginal) {
    console.log("No optimization to be made");
    return [
      ogLines,
      { before: lenOriginal, after: lenOriginal, ratio: 0, hasCrashed: false },
    ];
  }

  const [optimizedObjectsString, hasCrashed] = mergeMapObjectsToString(
    listOfBlocks,
    BLOCK_SIZE,
    objectsToKeep
  );

  const stats = {
    before: lenOriginal,
    after: lenOptimized,
    ratio: compressionRatio,
    hasCrashed,
  };

  const optimizedLines: string[] = [
    ...originalLines.slice(0, MAP_OBJECTS_INDEX),
    optimizedObjectsString,
    originalLines[MAP_OBJECTS_INDEX + 1],
  ];

  return [optimizedLines, stats];
}
