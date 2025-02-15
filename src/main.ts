// import "./style.css";
import { optimize } from "./bmmo/misc";

const loadMapFile_input = document.getElementById(
  "input_load_file"
) as HTMLInputElement;
const mapContent = document.getElementById(
  "map_content"
) as HTMLTextAreaElement;
const before_span = document.getElementById("before") as HTMLSpanElement;
const after_span = document.getElementById("after") as HTMLSpanElement;
const ratio_span = document.getElementById("ratio") as HTMLSpanElement;
const optimize_button = document.getElementById(
  "btn_optimize"
) as HTMLButtonElement;

let ogLines: string[] = [];

loadMapFile_input.addEventListener("change", async () => {
  const file = loadMapFile_input.files?.[0];
  ogLines = [];
  if (file) {
    const content = await file.text();
    ogLines.push(...content.split("\r\n"));
  }
});

optimize_button.addEventListener("click", () => {
  const [optimizedLines, stats] = optimize(ogLines);
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
