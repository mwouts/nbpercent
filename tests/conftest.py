from pathlib import Path

import pytest


def pytest_generate_tests(metafunc):
    if "ipynb_notebook_path" in metafunc.fixturenames:
        ids = []
        ipynb_notebook_paths = []
        for ipynb_notebook_path in (
            Path(__file__).parent / ".." / "examples" / "notebooks"
        ).iterdir():
            if ipynb_notebook_path.is_file():
                ipynb_notebook_paths.append(ipynb_notebook_path)
                ids.append(ipynb_notebook_path.stem)

        metafunc.parametrize("ipynb_notebook_path", ipynb_notebook_paths, ids=ids)


@pytest.fixture
def sample_ipynb_notebooks():
    return
