from pathlib import Path

from nbformat import read

from nbpercent.write import write


def test_write_sample_notebooks(sample_ipynb_notebooks):
    for ipynb_notebook_path in sample_ipynb_notebooks:
        notebook = read(ipynb_notebook_path, as_version=4)

        py_notebook_path = (
            Path(__file__).parent / "scripts" / (ipynb_notebook_path.stem + ".py")
        )
        write(notebook, py_notebook_path)
