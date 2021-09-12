from test.utils import TEST_LIPSUMFILE
import pytest

from src import lzw


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_DATA = {b"banana_bandana\n": b"ban\x81a_\x80nd\x83\n"}


def test_compress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.compress(cleartext)
        assert out == encoded


def test_decompress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.decompress(encoded)
        assert out == cleartext


def test_compress_decompress_should_negate(temp_dir):
    with open(temp_dir / TEST_LIPSUMFILE, "rb") as f:
        data = f.read()
    compressed = lzw.compress(data)
    decompressed = lzw.decompress(compressed)
    assert data == decompressed


@pytest.mark.slow
def test_benchmark_lzw_compression(lipsum_string, benchmark):
    compressed = benchmark(lzw.compress, lipsum_string)
    assert compressed


@pytest.mark.slow
def test_benchmark_lzw_decompression(lipsum_string, benchmark):
    compressed = lzw.compress(lipsum_string)
    decompressed = benchmark(lzw.decompress, compressed)
    assert decompressed
