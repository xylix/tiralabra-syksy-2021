from src import lzw
import pytest


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_COMPRESS_DATA = {"banana_bandana\n": "98,97,110,129,97,95,128,110,100,131"}


def test_compress():
    for inp, outp in TEST_COMPRESS_DATA.items():
        out = lzw.compress(inp)
        assert out == outp


TEST_DECOMPRESS_DATA = {"98,97,110,129,97,95,128,110,100,131": "ban98aa_98bnd1109"}


def test_decompress():
    for inp, outp in TEST_DECOMPRESS_DATA.items():
        out = lzw.decompress(inp)
        assert out == outp


def test_compress_decompress_should_negate():
    test_str = "asdasdasdasdabcabc"
    compressed = lzw.compress(test_str)
    decompressed = lzw.decompress(compressed)
    assert decompressed == test_str


def test_main_invalid_input():
    with pytest.raises(Exception) as excinfo:
        lzw.main("nonexistent.txt", True, True, True, False)
