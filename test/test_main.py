import itertools
from test.utils import TEST_INFILE

from src import main


def test_main_invalid_input():
    main.main("nonexistent.txt", True, True, True, False, main.Algorithm.LZW)
    main.main("nonexistent.txt.lzw", True, False, True, False, main.Algorithm.LZW)


def test_permutations_of_main_args(temp_dir):
    l = [False, True]
    bools = [list(i) for i in itertools.product(l, repeat=4)]
    for permutation in bools:
        main.main(str(temp_dir / TEST_INFILE), *permutation)
