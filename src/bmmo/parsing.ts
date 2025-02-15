import { BlocksTable } from "./blocks_table";

/** Given a bmap, get the width and height of the map */
export function getBmapMeasures(bmap: Record<string, any>): [number, number] {
  const config = bmap["Config"];
  return [parseInt(config["MapWidth"]), parseInt(config["MapHeight"])];
}

/** Given a bmap, separate the blocks/walls and all other objects.
 * @returns [a list of blocks/walls, a list of all other objects]
 */
export function separateObjectsFromOtherObjects(
  bmap: Record<string, any>,
  objsToSeparateNames: string[]
): [Record<string, any>[], Record<string, any>[]] {
  const blocksList: Record<string, any>[] = [];
  const othersList: Record<string, any>[] = [];

  for (const [key, obj] of Object.entries(bmap)) {
    if (key !== "Config" && objsToSeparateNames.includes(obj["Name"])) {
      blocksList.push(obj);
    } else {
      othersList.push(obj);
    }
  }

  return [blocksList, othersList];
}

function createTable(width: number, height: number): number[][] {
  const row = Array(width).fill(0);
  const columns = Array(height)
    .fill(null)
    .map(() => [...row]);
  return columns;
}

function getCoordinatesAndSizes(
  block: Record<string, any>,
  wallName: string,
  blocksInfo: Record<string, Record<string, number>>
): [number, number, number, number] {
  const x = block["X"];
  const y = block["Y"];
  if (block["Name"] === wallName) {
    return [
      parseInt(x),
      parseInt(y),
      parseInt(block["ObjWallWidth"]),
      parseInt(block["ObjWallHeight"]),
    ];
  }

  const blockInfo = blocksInfo[block["Name"]];
  return [parseInt(x), parseInt(y), blockInfo["width"], blockInfo["height"]];
}

function getIndexBlocksTableBasedOnTypeSound(
  listOfBlocksTable: BlocksTable[],
  block: Record<string, any>
): number {
  for (let i = 0; i < listOfBlocksTable.length; i++) {
    const blocksTable = listOfBlocksTable[i];
    if (
      blocksTable.type === block["ObjType"] &&
      blocksTable.sound === block["ObjSound"]
    ) {
      return i;
    }
  }
  return -1;
}

function isDivisible(dividend: number, divisor: number): boolean {
  return dividend % divisor === 0;
}

/**
 * Given a list of blocks, it returns a list of table of blocks.
 * There are as many tables as there are different types or sounds of blocks.
 *
 * @param mapWidth width of the map, blocks outside of the given width will not be in the table
 * @param mapHeight height of the map, blocks outside of the given height will not be in the table
 * @param blocksList blocks to put in the table
 * @param wallName name of the wall tool
 * @param blocksInfo list of the different blocks information
 * @param blockSize used to scale the sizes and coordinates, advised to use if blocks are snapped to the map grid
 *
 * @returns A list of BlocksTable. A table is composed of 0 & 1. 1 represents the presence of a block.
 */
export function fromBlocksToListOfBlocksTable(
  mapWidth: number,
  mapHeight: number,
  blocksList: Record<string, any>[],
  wallName: string,
  blocksInfo: Record<string, Record<string, number>>,
  blockSize: number = 1
): BlocksTable[] {
  const scaledMapWidth = Math.floor(mapWidth / blockSize);
  const scaledMapHeight = Math.floor(mapHeight / blockSize);
  const table = createTable(scaledMapWidth, scaledMapHeight);

  const listOfBlocksTable: BlocksTable[] = [];

  function checkCoordinates(x: number, y: number): boolean {
    return x >= 0 && x < scaledMapWidth && y >= 0 && y < scaledMapHeight;
  }

  function updateBlocksTable(
    x: number,
    y: number,
    w: number,
    h: number,
    blocksTable: BlocksTable
  ): void {
    const scaledX = Math.floor(x / blockSize);
    const scaledY = Math.floor(y / blockSize);
    const scaledW = Math.floor(w / blockSize);
    const scaledH = Math.floor(h / blockSize);

    for (let j = scaledY; j < scaledY + scaledH; j++) {
      for (let i = scaledX; i < scaledX + scaledW; i++) {
        if (checkCoordinates(i, j)) {
          blocksTable.table[j][i] = 1;
        }
      }
    }
  }

  function areCoordinatesUsable(x: number, y: number): boolean {
    if (!isDivisible(x, blockSize) || !isDivisible(y, blockSize)) return false;
    const scaledX = Math.floor(x / blockSize);
    const scaledY = Math.floor(y / blockSize);
    return checkCoordinates(scaledX, scaledY);
  }

  for (const block of blocksList) {
    const [x, y, width, height] = getCoordinatesAndSizes(
      block,
      wallName,
      blocksInfo
    );
    if (!areCoordinatesUsable(x, y)) continue;

    let index = getIndexBlocksTableBasedOnTypeSound(listOfBlocksTable, block);
    if (index === -1) {
      index = listOfBlocksTable.length;
      listOfBlocksTable.push(
        new BlocksTable(
          block["ObjType"],
          block["ObjSound"],
          JSON.parse(JSON.stringify(table))
        )
      );
    }

    updateBlocksTable(x, y, width, height, listOfBlocksTable[index]);
  }

  return listOfBlocksTable;
}
