import pytest

from src import huffman, lzw


compression_results = ""


@pytest.mark.slow
def test_huff_holmes(holmes):
    compressed = huffman.compress(holmes)
    decompressed = huffman.decompress(compressed)
    assert holmes == decompressed


@pytest.mark.slow
def test_benchmark_huffman_compression(lipsum, benchmark):
    compressed = benchmark(huffman.compress, lipsum)
    assert compressed


@pytest.mark.slow
def test_benchmark_huffman_decompression(lipsum, benchmark):
    compressed = huffman.compress(lipsum)
    decompressed = benchmark(huffman.decompress, compressed)
    assert decompressed


@pytest.mark.slow
def test_lzw_holmes(holmes):
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


@pytest.mark.slow
def test_combo_holmes(holmes):
    compressed = huffman.compress(lzw.compress(holmes))
    decompressed = lzw.decompress(huffman.decompress(compressed))
    assert holmes == decompressed
