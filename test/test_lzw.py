from test.utils import TEST_LIPSUMFILE
import pytest

from src import lzw


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_DATA = {
    b"banana_bandana\n": b"\x80\x04\x95\x1b\x00\x00\x00\x00\x00\x00\x00]\x94(KbKaKnK\x81KaK_K\x80KnKdK\x83K\ne."
}


def test_compress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.compress(cleartext)
        assert out == encoded


def test_decompress():
    for cleartext, encoded in TEST_DATA.items():
        out = lzw.decompress(encoded)
        assert out == cleartext


def test_compress_decompress_should_negate(lipsum):
    compressed = lzw.compress(lipsum)
    decompressed = lzw.decompress(compressed)
    assert lipsum == decompressed


@pytest.mark.skip("This is currently too slow to run")
def test_holmes(holmes):
    compressed = lzw.compress(holmes)
    decompressed = lzw.decompress(compressed)
    assert holmes == decompressed


@pytest.mark.slow
def test_benchmark_lzw_compression(lipsum, benchmark):
    compressed = benchmark(lzw.compress, lipsum)
    assert compressed


@pytest.mark.slow
def test_benchmark_lzw_decompression(lipsum, benchmark):
    compressed = lzw.compress(lipsum)
    decompressed = benchmark(lzw.decompress, compressed)
    assert decompressed
