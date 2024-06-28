from browser import bind, window, document
from bmmo import main as cli_main

load_btn = document["input_load_file"]
optimize_btn = document["btn_optimize"]
s = document["btn_save_file"]
map_content = document["map_content"]
span_before = document["before"]
span_after = document["after"]
span_ratio = document["ratio"]
og_lines: list[str] = []
optimized_lines: list[str] = []

@bind(load_btn, "input")
def file_read(ev):
    def onload(event):
        """Triggered when file is read. The FileReader instance is
        event.target.
        The file content, as text, is the FileReader instance's "result"
        attribute."""
        lines = event.target.result.__str__().splitlines()
        # optimized_lines = cli_main.optimize(lines)
        # joined_string = "\n".join(optimized_lines)
        # map_content.value = joined_string
        for line in lines:
            og_lines.append(line)
        # enable the optimize button
        del optimize_btn.attrs['disabled']

    optimize_btn.attrs["disabled"] = "true"
    # Get the selected file as a DOM File object
    file = load_btn.files[0]
    # Create a new DOM FileReader instance
    reader = window.FileReader.new()
    # Read the file content as text
    reader.readAsText(file)
    reader.bind("load", onload)


@bind(optimize_btn, "mousedown")
def mousedown(evt):
      """Create a "data URI" to set the downloaded file content
      Cf. https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/Data_URIs
      """
      optimized_lines, stats = cli_main.optimize(og_lines)
      if stats['has_crashed']:
        new_lines = []
        for line in optimized_lines:
            new_lines.append(window.JSONdumps(line))
        optimized_lines = new_lines
      joined_string = "\n".join(optimized_lines)
      map_content.value = joined_string
      span_before.textContent = stats["before"]
      span_after.textContent = stats["after"]
      span_ratio.textContent = stats["ratio"]