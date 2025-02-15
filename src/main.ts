// import "./style.css";
import { optimizeAndDraw } from "./drawing/drawing";

const loadMapFile_input = document.getElementById(
  "input_load_file"
) as HTMLInputElement;
const mapContent = document.getElementById(
  "map_content"
) as HTMLTextAreaElement;
const before_span = document.getElementById("before") as HTMLSpanElement;
const after_span = document.getElementById("after") as HTMLSpanElement;
const ratio_span = document.getElementById("ratio") as HTMLSpanElement;
const ogMapCanvas = document.getElementById(
  "og_map_canvas"
) as HTMLCanvasElement;
const optimizedMapCanvas = document.getElementById(
  "optimized_map_canvas"
) as HTMLCanvasElement;

let ogLines: string[] = [];

loadMapFile_input.addEventListener("change", async () => {
  const file = loadMapFile_input.files?.[0];
  ogLines = [];

  if (!file) return;

  const content = await file.text();
  ogLines.push(...content.split("\r\n"));

  const [optimizedLines, stats] = optimizeAndDraw(
    ogLines,
    ogMapCanvas,
    optimizedMapCanvas
  );
  if (stats["has_crashed"]) {
    alert(
      "The optimization has crashed! This map is not suitable for optimization."
    );
    return;
  }

  mapContent.value = optimizedLines.join("\n");
  before_span.textContent = stats["before"].toString();
  after_span.textContent = stats["after"].toString();
  ratio_span.textContent = stats["ratio"].toString();
});
