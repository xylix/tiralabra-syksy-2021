from io import UnsupportedOperation
import itertools

import pytest

from src import main
from test.utils import TEST_INFILE, TEST_OUTFILE_HUFFMAN, TEST_OUTFILE_LZW


def test_main_invalid_input():
    with pytest.raises(FileNotFoundError):
        main.main("nonexistent.txt", True, False, main.Algorithm.LZW)

    with pytest.raises(TypeError):
        main.main("nonexistent.txt", True, False, "totally_not_an_algorithm")

    with pytest.raises(FileNotFoundError):
        main.main(
            "nonexistent.txt.lzw",
            True,
            False,
            main.Algorithm.LZW,
        )
    with pytest.raises(FileNotFoundError):
        main.main("nonexistent.txt", True, False, main.Algorithm.LZW)


def test_permutations_of_main_args(temp_dir):
    files = [
        str(temp_dir / TEST_INFILE),
        str(temp_dir / TEST_OUTFILE_LZW),
        str(temp_dir / TEST_OUTFILE_HUFFMAN),
    ]

    l = [False, True]
    bools = [list(i) for i in itertools.product(l, repeat=2)]
    # We need the bools in reverse order so the configuration that writes to file is first
    bools.reverse()
    for permutation in bools:
        for infile in files:
            for algo in main.Algorithm:
                main.main(infile, *permutation, algo)
