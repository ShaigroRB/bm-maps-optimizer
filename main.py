from browser import bind, window, document
from bmmo import main as cli_main

load_btn = document["input_load_file"]
optimize_btn = document["btn_optimize"]
og_lines: list[str] = []
optimized_lines: list[str] = []
map_content = document["map_content"]

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
      optimized_lines = cli_main.optimize(og_lines)
      joined_string = "\n".join(optimized_lines)
      map_content.value = joined_string