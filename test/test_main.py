from io import UnsupportedOperation
import itertools

import pytest

from src import main
from test.utils import TEST_INFILE


def test_main_invalid_input():
    with pytest.raises(FileNotFoundError):
        main.main(
            "nonexistent.txt", main.Operation.archive, True, False, main.Algorithm.lzw
        )
    with pytest.raises(UnsupportedOperation):
        main.main(
            "nonexistent.txt.lzw",
            main.Operation.archive,
            True,
            False,
            main.Algorithm.lzw,
        )
    with pytest.raises(TypeError):
        main.main(
            "nonexistent.txt", "not_correct_enum", True, False, main.Algorithm.lzw
        )


def test_permutations_of_main_args(temp_dir):
    l = [False, True]
    bools = [list(i) for i in itertools.product(l, repeat=2)]
    for permutation in bools:
        for operation in main.Operation:
            for algo in main.Algorithm:
                main.main(str(temp_dir / TEST_INFILE), operation, *permutation, algo)
