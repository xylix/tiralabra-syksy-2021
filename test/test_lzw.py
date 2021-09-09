from typing import Iterator
from src import lzw
import pytest
import itertools
import tempfile
from shutil import copyfile
from pathlib import Path


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_DATA = {"banana_bandana\n": "98,97,110,129,97,95,128,110,100,131,10"}
TEST_INFILE = "test_file.txt"
TEST_OUTFILE = "test_file.txt.lzw"
TEST_LIPSUMFILE = "test_lipsum_10_paragraphs.txt"


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


def test_compress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.compress(cleartext)
        assert out == encoded


def test_decompress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.decompress(encoded)
        assert out == cleartext


def test_compress_decompress_should_negate(temp_dir):
    with open(temp_dir / TEST_LIPSUMFILE) as f:
        data = f.read()
    compressed = lzw.compress(data)
    decompressed = lzw.decompress(compressed)
    assert data == decompressed


def test_main_invalid_input():
    lzw.main("nonexistent.txt", True, True, True, False)
    lzw.main("nonexistent.txt.lzw", True, False, True, False)


def test_permutations_of_main_args(temp_dir):
    l = [False, True]
    bools = [list(i) for i in itertools.product(l, repeat=4)]
    for permutation in bools:
        lzw.main(str(temp_dir / TEST_INFILE), *permutation)
