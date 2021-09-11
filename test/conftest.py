from pathlib import Path
from shutil import copyfile
import tempfile
from test.test_huffmann import TEST_LIPSUMFILE
from test.utils import TEST_INFILE, TEST_OUTFILE
from typing import Iterator

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture
def temp_dir() -> Iterator[Path]:
    with tempfile.TemporaryDirectory() as dirname:
        copyfile(Path(__file__).parent / TEST_INFILE, Path(dirname) / TEST_INFILE)
        copyfile(Path(__file__).parent / TEST_OUTFILE, Path(dirname) / TEST_OUTFILE)
        copyfile(
            Path(__file__).parent / TEST_LIPSUMFILE,
            Path(dirname) / "test_lipsum_10_paragraphs.txt",
        )
        yield Path(dirname)


@pytest.fixture
def lipsum_string() -> str:
    with open(Path(__file__).parent / TEST_LIPSUMFILE) as f:
        data = f.read()
    return data
