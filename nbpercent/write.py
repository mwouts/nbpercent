import base64
import json
from copy import copy
from pathlib import Path

import yaml
from nbformat.notebooknode import NotebookNode

COMMENT_CHAR = "#"

OUTPUT_EXTENSIONS = {
    "text/plain": "txt",
    "text/markdown": "md",
    "text/html": "html",
    "image/png": "png",
    "application/javascript": "js",
}


def comment_out(text):
    return [COMMENT_CHAR + " " + line for line in text]


def as_dict(metadata):
    if isinstance(metadata, NotebookNode):
        return {key: as_dict(value) for key, value in metadata.items()}
    return metadata


def notebook_header(metadata):
    return comment_out(
        ["---"] + yaml.safe_dump({"jupyter": as_dict(metadata)}).splitlines() + ["---"]
    )


def cell_header(cell):
    if cell.cell_type == "code":
        cell_type = "%%"
    elif cell.cell_type == "markdown":
        cell_type = "%% [markdown]"
    elif cell.cell_type == "raw":
        cell_type = "%% [raw]"
    else:
        raise NotImplementedError(cell.cell_type)

    header = [cell_type, cell.id]
    if cell.metadata:
        header.append(
            " ".join(
                f"{key}={json.dumps(value)}"
                for key, value in sorted(cell.metadata.items())
            )
        )

    return COMMENT_CHAR + " " + " ".join(header)


def write_output(output, output_count, notebook_path, cell_id):
    output = copy(output)
    out_prefix = f"{COMMENT_CHAR} {chr(171)}{chr(187)}"

    def export_to_file(output, key, extension, b64decode=False):
        output_file = f"{cell_id}_{output_count}.{extension}"
        output_folder = notebook_path.parent / (notebook_path.stem + "_outputs")
        output_folder.mkdir(exist_ok=True)
        output_path = output_folder / output_file
        if b64decode:
            output_path.write_bytes(base64.b64decode(output[key]))
        else:
            output_path.write_text(output[key])
        output[key] = output_file

    def encode_output(output):
        return [out_prefix] + comment_out(yaml.safe_dump(as_dict(output)).splitlines())

    if output["output_type"] == "stream":
        export_to_file(output, "text", extension="stream")
        return encode_output(output)

    if output["output_type"] == "error":
        output["traceback"] = "\n".join(output["traceback"]) + "\n"
        export_to_file(output, "traceback", extension="traceback")
        return encode_output(output)

    data = output["data"]
    execution_count = output.pop("execution_count", None)

    if not output["metadata"]:
        del output["metadata"]

    if execution_count is not None:
        if output["output_type"] == "execute_result":
            del output["output_type"]

        out_prefix = f"{COMMENT_CHAR} {chr(171)}{execution_count}{chr(187)}"
    else:
        if output["output_type"] == "display_data":
            del output["output_type"]

    # single small output are inlined
    if (
        set(output.keys()) == {"data"}
        and set(data.keys()) == {"text/plain"}
        and len(data["text/plain"]) < 75
        and "\n" not in data["text/plain"]
    ):
        return [f"{out_prefix} {data['text/plain']}"]

    # other outputs are exported to the disk
    for key, value in data.items():
        # Plotly and ipywidgets
        if key.endswith("+json"):
            extension = "json"
        else:
            extension = OUTPUT_EXTENSIONS[key]

        if isinstance(value, NotebookNode):
            data[key] = json.dumps(as_dict(value))

        export_to_file(data, key, extension, b64decode=(key == "image/png"))

    return encode_output(output)


def write(notebook, notebook_path):
    """Write the notebook as a percent script with outputs at the given path"""
    notebook_path = Path(notebook_path)

    # Notebook metadata
    script = notebook_header(notebook.metadata)
    script.append("")

    # Notebook cells
    for cell in notebook.cells:
        script.append(cell_header(cell))
        if cell.cell_type != "code":
            script.extend(comment_out(cell.source.splitlines()))
            script.append("")
        else:
            script.extend(cell.source.splitlines())
            script.append("")

            # add outputs
            for output_count, output in enumerate(cell.outputs):
                script.extend(
                    write_output(
                        output=output,
                        output_count=output_count,
                        notebook_path=notebook_path,
                        cell_id=cell.id,
                    )
                )

            if cell.outputs:
                script.append("")

    notebook_path.write_text("\n".join(script))
