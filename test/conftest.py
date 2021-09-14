from pathlib import Path
from shutil import copyfile
import tempfile
from typing import Iterator

import pytest

from test.utils import TEST_INFILE, TEST_LIPSUMFILE, TEST_OUTFILE

RESOURCES = Path(__file__).parent / "resources"


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
        copyfile(
            RESOURCES / TEST_INFILE,
            Path(dirname) / TEST_INFILE,
        )
        copyfile(
            RESOURCES / TEST_OUTFILE,
            Path(dirname) / TEST_OUTFILE,
        )
        copyfile(
            RESOURCES / TEST_LIPSUMFILE,
            Path(dirname) / "test_lipsum_10_paragraphs.txt",
        )
        yield Path(dirname)


@pytest.fixture
def lipsum() -> bytes:
    with open(RESOURCES / TEST_LIPSUMFILE, "rb") as f:
        data = f.read()
    return data


@pytest.fixture
def holmes() -> bytes:
    with open(RESOURCES / "holmes.txt", "rb") as f:
        data = f.read()
    return data
