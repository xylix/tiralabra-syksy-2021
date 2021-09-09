from typing import Iterator
from src import lzw
import pytest
import itertools
import tempfile
from shutil import copyfile
from pathlib import Path


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_DATA = {"banana_bandana\n": "98,97,110,129,97,95,128,110,100,131,10"}
TEST_INFILE = Path(__file__).parent / "test_file.txt"
TEST_OUTFILE = Path(__file__).parent / "test_file.txt.lzw"


@pytest.fixture
def temp_file() -> Iterator[Path]:
    with tempfile.TemporaryDirectory() as dirname:
        copyfile(TEST_INFILE, Path(dirname) / "test_file.txt")
        copyfile(TEST_OUTFILE, Path(dirname) / "test_file.txt.lzw")
        tmp_file_path = Path(dirname) / "test_file.txt"
        yield tmp_file_path


def test_compress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.compress(cleartext)
        assert out == encoded


def test_decompress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.decompress(encoded)
        assert out == cleartext


def test_compress_decompress_should_negate():
    test_str = "a_normal_word"
    compressed = lzw.compress(test_str)
    decompressed = lzw.decompress(compressed)
    assert decompressed == test_str


def test_main_invalid_input():
    lzw.main("nonexistent.txt", True, True, True, False)
    lzw.main("nonexistent.txt.lzw", True, False, True, False)


def test_permutations_of_main_args(temp_file):
    l = [False, True]
    bools = [list(i) for i in itertools.product(l, repeat=4)]
    for permutation in bools:
        if permutation[1]:
            f"{temp_file}.lzw"
        lzw.main(str(temp_file), *permutation)
