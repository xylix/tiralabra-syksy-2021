from src import lzw
import pytest


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_DATA = {"banana_bandana\n": "98,97,110,129,97,95,128,110,100,131,10"}


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
    with pytest.raises(Exception) as _:
        lzw.main("nonexistent.txt", True, True, True, False)
