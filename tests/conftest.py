import pytest
from pathlib import Path


@pytest.fixture
def sample_ipynb_notebooks():
    return (Path(__file__).parent / "notebooks").iterdir()
