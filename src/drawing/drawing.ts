import {
  MAP_OBJECTS_INDEX,
  BLOCK_SIZE as BLOCK_SIZE_128PX,
  BLOCKS_AND_WALL_NAMES,
  WALL_TOOL,
  BLOCKS,
} from "../bmmo/constants";
import {
  getBmapMeasures,
  separateObjectsFromOtherObjects,
  fromBlocksToListOfBlocksTable,
  getCoordinatesAndSizes,
} from "../bmmo/parsing";
import { getLeastBlocksFromBlocksTable } from "../bmmo/optimization";
import { Block } from "../bmmo/block";
import { mergeMapObjectsToString } from "../bmmo/misc";
import { COLORS_PER_TYPE } from "./colors";

const SCALE_BLOCK_SIZE = 32;
const BLOCK_SIZE = BLOCK_SIZE_128PX / SCALE_BLOCK_SIZE;
const DRAWN_BLOCK_SIZE_PX = 20 / SCALE_BLOCK_SIZE;

const progress = document.getElementById("progress") as HTMLProgressElement;

// @ts-ignore -- Useful for debugging
function printTable(table: number[][]): void {
  let content = "";
  table.forEach((row) => {
    content += row.map((nb) => (nb === 1 ? "🔳" : "◼️")).join(" ") + "\n";
  });
  console.log(content);
}

export function optimizeAndDraw(
  ogLines: string[],
  ogCanvas: HTMLCanvasElement,
  optimizedCanvas: HTMLCanvasElement
): [string[], Record<string, number | boolean>] {
  console.clear();
  progress.value = 0;

  const originalLines = ogLines;
  const bmapJson = JSON.parse(originalLines[MAP_OBJECTS_INDEX]);
  const [_mapWidth, _mapHeight] = getBmapMeasures(bmapJson);

  const [blocksToOptimize, objectsToKeep] = separateObjectsFromOtherObjects(
    bmapJson,
    BLOCKS_AND_WALL_NAMES
  );

  progress.value = 5;

  const listOfBlocksTable = fromBlocksToListOfBlocksTable(
    _mapWidth,
    _mapHeight,
    blocksToOptimize,
    WALL_TOOL,
    BLOCKS,
    BLOCK_SIZE
  );

  progress.value = 15;

  // set the width and height of the canvas
  ogCanvas.width = (_mapWidth / BLOCK_SIZE) * DRAWN_BLOCK_SIZE_PX;
  ogCanvas.height = (_mapHeight / BLOCK_SIZE) * DRAWN_BLOCK_SIZE_PX;
  optimizedCanvas.width = ogCanvas.width;
  optimizedCanvas.height = ogCanvas.height;

  const ogCanvasCtx = ogCanvas.getContext("2d") as CanvasRenderingContext2D;
  const optimizedCanvasCtx = optimizedCanvas.getContext(
    "2d"
  ) as CanvasRenderingContext2D;

  // ogCanvasCtx.scale(1 / BLOCK_SIZE, 1 / BLOCK_SIZE);
  // optimizedCanvasCtx.scale(1 / BLOCK_SIZE, 1 / BLOCK_SIZE);

  // render the original map from blocksToOptimize to have all the og blocks with their original sizes
  blocksToOptimize.forEach((block) => {
    const [x, y, width, height] = getCoordinatesAndSizes(
      block,
      WALL_TOOL,
      BLOCKS
    );
    const [scaledX, scaledY, scaledWidth, scaledHeight] = [
      Math.floor(x / BLOCK_SIZE),
      Math.floor(y / BLOCK_SIZE),
      Math.floor(width / BLOCK_SIZE),
      Math.floor(height / BLOCK_SIZE),
    ];

    // draw outline behind the actual block
    ogCanvasCtx.fillStyle = "blue";

    if (scaledWidth === 0 || scaledHeight === 0) {
      console.log(
        `x: ${x}, y: ${y}, width: ${width}, height: ${height}, scaledX: ${scaledX}, scaledY: ${scaledY}, scaledWidth: ${scaledWidth}, scaledHeight: ${scaledHeight}`
      );
      ogCanvasCtx.fillStyle = "red"; // signifies error
    }

    ogCanvasCtx.fillRect(
      scaledX * DRAWN_BLOCK_SIZE_PX,
      scaledY * DRAWN_BLOCK_SIZE_PX,
      scaledWidth * DRAWN_BLOCK_SIZE_PX,
      scaledHeight * DRAWN_BLOCK_SIZE_PX
    );

    // draw the actual block
    ogCanvasCtx.fillStyle = COLORS_PER_TYPE[block["ObjType"]];
    ogCanvasCtx.fillRect(
      scaledX * DRAWN_BLOCK_SIZE_PX + 2,
      scaledY * DRAWN_BLOCK_SIZE_PX + 2,
      scaledWidth * DRAWN_BLOCK_SIZE_PX - 4,
      scaledHeight * DRAWN_BLOCK_SIZE_PX - 4
    );
  });

  // listOfBlocksTable.forEach((blocksTable) => {
  //   console.log(`Type: ${blocksTable.type}, Sound: ${blocksTable.sound}`);
  //   // display nb of rows & columns
  //   printTable(blocksTable.table);
  // });

  let incr = 80 / listOfBlocksTable.length;

  let listOfBlocks: Block[] = [];

  listOfBlocksTable.forEach((blocksTable) => {
    const currBlocks = getLeastBlocksFromBlocksTable(blocksTable);
    listOfBlocks = [...listOfBlocks, ...currBlocks];

    progress.value += incr;

    currBlocks.forEach((block) => {
      const { x, y, width, height } = block;

      // draw outline behind the actual block
      optimizedCanvasCtx.fillStyle = "black";
      optimizedCanvasCtx.fillRect(
        x * DRAWN_BLOCK_SIZE_PX,
        y * DRAWN_BLOCK_SIZE_PX,
        DRAWN_BLOCK_SIZE_PX * width,
        DRAWN_BLOCK_SIZE_PX * height
      );

      // draw the actual block
      optimizedCanvasCtx.fillStyle = COLORS_PER_TYPE[blocksTable.type];
      optimizedCanvasCtx.fillRect(
        x * DRAWN_BLOCK_SIZE_PX + 2,
        y * DRAWN_BLOCK_SIZE_PX + 2,
        DRAWN_BLOCK_SIZE_PX * width - 4,
        DRAWN_BLOCK_SIZE_PX * height - 4
      );
    });
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

  progress.value = 100;

  return [optimizedLines, stats];
}
