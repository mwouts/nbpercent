from nbformat import read

from nbpercent.write import write


def test_write_sample_notebooks(ipynb_notebook_path):
    notebook = read(ipynb_notebook_path, as_version=4)

    py_notebook_path = (
        ipynb_notebook_path.parent
        / ".."
        / "percent_with_outputs"
        / (ipynb_notebook_path.stem + ".py")
    )
    write(notebook, py_notebook_path)
