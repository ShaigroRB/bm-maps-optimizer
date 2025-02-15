import { BlocksTable } from "./blocks_table";
import { Block } from "./block";

function isCellValid(cell: number): boolean {
  return cell === 1;
}

function findCoordinatesOfMostTopLeftValidCell(
  table: number[][]
): [number, number] {
  const rowLength = table.length;
  const columnLength = rowLength > 0 ? table[0].length : 0;

  for (let i = 0; i < columnLength; i++) {
    for (let j = 0; j < rowLength; j++) {
      if (isCellValid(table[j][i])) {
        return [i, j];
      }
    }
  }

  return [-1, -1];
}

function isRowStartToEndValid(
  table: number[][],
  rowIndex: number,
  startIndex: number,
  endIndex: number
): boolean {
  for (let i = startIndex; i < endIndex; i++) {
    if (!isCellValid(table[rowIndex][i])) {
      return false;
    }
  }
  return true;
}

function removeBlockFromTable(block: Block, table: number[][]): void {
  for (let j = block.y; j < block.height + block.y; j++) {
    for (let i = block.x; i < block.width + block.x; i++) {
      table[j][i] = 0;
    }
  }
}

/**
 * The idea is to get the most top left block.
 * We try to expand its width on its right as much as possible.
 * Once it's not possible anymore, we expand its height on the bottom as much as possible while keeping the same width.
 * When we cannot expand it anymore because the width is not maintained or the maximum height has been reached, we create
 * a block with the new width and height.
 * Now, we can remove the newly created block from the given table of blocks.
 * Finally, we repeat the process.
 * Technically speaking, it doesn't get the least blocks possible. But in our use case, it's good enough.
 */
export function getLeastBlocksFromBlocksTable(
  blocksTable: BlocksTable
): Block[] {
  const blockType = blocksTable.type;
  const blockSound = blocksTable.sound;
  const nbRows = blocksTable.table.length;
  const nbColumns = blocksTable.table[0].length;
  const blocks: Block[] = [];
  const optimizedTable = JSON.parse(JSON.stringify(blocksTable.table)); // Deep copy

  function createBlock(x: number, y: number, w: number, h: number): Block {
    return new Block(x, y, w, h, blockType, blockSound);
  }

  // for a more modular algorithm, add the find coordinates as a function given as parameter
  let [topLeftCellX, topLeftCellY] =
    findCoordinatesOfMostTopLeftValidCell(optimizedTable);
  let indexRow = topLeftCellY;
  let indexCol = topLeftCellX + 1;

  while (topLeftCellX !== -1 && topLeftCellY !== -1) {
    let currentCellIsValid = true;

    // Get the index of the first invalid cell from left to right
    // last valid index is: (invalid_index - 1)
    while (indexCol < nbColumns && currentCellIsValid) {
      const currentCell = optimizedTable[indexRow][indexCol];
      currentCellIsValid = isCellValid(currentCell);
      if (currentCellIsValid) {
        indexCol++;
      }
    }

    const indexInvalidCell = indexCol;
    indexRow++;
    let currentRowIsValid = true;

    // Get the index of the first invalid row (top to bottom)
    while (indexRow < nbRows && currentRowIsValid) {
      currentRowIsValid = isRowStartToEndValid(
        optimizedTable,
        indexRow,
        topLeftCellX,
        indexInvalidCell
      );
      if (currentRowIsValid) {
        indexRow++;
      }
    }

    const indexInvalidRow = indexRow;

    const blockWidth = indexInvalidCell - topLeftCellX;
    const blockHeight = indexInvalidRow - topLeftCellY;
    const block = createBlock(
      topLeftCellX,
      topLeftCellY,
      blockWidth,
      blockHeight
    );

    blocks.push(block);
    removeBlockFromTable(block, optimizedTable);

    [topLeftCellX, topLeftCellY] =
      findCoordinatesOfMostTopLeftValidCell(optimizedTable);
    indexRow = topLeftCellY;
    indexCol = topLeftCellX + 1;
  }

  return blocks;
}
