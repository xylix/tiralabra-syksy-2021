from pathlib import Path
import pickle

import pytest

from src import huffman
from src.huffman import HuffmanResult, Node

# fmt: off
TEST_DATA = {
    b"FIRST_SIMPLE_TEST_STRING": HuffmanResult(encoded=3115303770153516478818454, bintree=Node(freq=24, symbol=None, left=Node(freq=9, symbol=None, left=Node(freq=4, symbol=84, left=None, right=None), right=Node(freq=5, symbol=None, left=Node(freq=2, symbol=None, left=Node(freq=1, symbol=78, left=None, right=None), right=Node(freq=1, symbol=76, left=None, right=None)), right=Node(freq=3, symbol=95, left=None, right=None))), right=Node(freq=15, symbol=None, left=Node(freq=7, symbol=None, left=Node(freq=3, symbol=73, left=None, right=None), right=Node(freq=4, symbol=None, left=Node(freq=2, symbol=None, left=Node(freq=1, symbol=70, left=None, right=None), right=Node(freq=1, symbol=77, left=None, right=None)), right=Node(freq=2, symbol=None, left=Node(freq=1, symbol=71, left=None, right=None), right=Node(freq=1, symbol=80, left=None, right=None)))), right=Node(freq=8, symbol=None, left=Node(freq=4, symbol=83, left=None, right=None), right=Node(freq=4, symbol=None, left=Node(freq=2, symbol=82, left=None, right=None), right=Node(freq=2, symbol=69, left=None, right=None))))))

    # HuffmanResult(encoded=b'1010010011101100001111010010101101110101111101100111111000011110001110100010010110', bintree=Node(freq=24, symbol=None, left=Node(freq=9, symbol=None, left=Node(freq=4, symbol='T', left=None, right=None), right=Node(freq=5, symbol=None, left=Node(freq=2, symbol=None, left=Node(freq=1, symbol='N', left=None, right=None), right=Node(freq=1, symbol='L', left=None, right=None)), right=Node(freq=3, symbol='_', left=None, right=None))), right=Node(freq=15, symbol=None, left=Node(freq=7, symbol=None, left=Node(freq=3, symbol='I', left=None, right=None), right=Node(freq=4, symbol=None, left=Node(freq=2, symbol=None, left=Node(freq=1, symbol='F', left=None, right=None), right=Node(freq=1, symbol='M', left=None, right=None)), right=Node(freq=2, symbol=None, left=Node(freq=1, symbol='G', left=None, right=None), right=Node(freq=1, symbol='P', left=None, right=None)))), right=Node(freq=8, symbol=None, left=Node(freq=4, symbol='S', left=None, right=None), right=Node(freq=4, symbol=None, left=Node(freq=2, symbol='R', left=None, right=None), right=Node(freq=2, symbol='E', left=None, right=None))))))
}
# fmt: on

TEST_LIPSUMFILE = "test_lipsum_10_paragraphs.txt"


@pytest.fixture
def lipsum_string() -> str:
    with open(Path(__file__).parent / TEST_LIPSUMFILE) as f:
        data = f.read()
    return data


def test_preprocess():
    for cleartext, encoded in TEST_DATA.items():
        out = huffman.preprocess(cleartext)
        assert out


def test_compress():
    for cleartext, expected_output in TEST_DATA.items():
        out = huffman.compress(cleartext)
        assert pickle.loads(out) == expected_output


def test_decompress():
    for cleartext, expected_output in TEST_DATA.items():
        out = huffman.decompress(pickle.dumps(expected_output))
        assert out == cleartext


def test_longer_input_file():
    with open(Path(__file__).parent / TEST_LIPSUMFILE, "rb") as f:
        data = f.read()
    compressed = huffman.compress(data)
    decompressed = huffman.decompress(compressed)
    assert data == decompressed


@pytest.mark.slow
def test_benchmark_huffman_compression(lipsum_string, benchmark):
    compressed = benchmark(huffman.compress, lipsum_string)


@pytest.mark.slow
def test_benchmark_huffman_decompression(lipsum_string, benchmark):
    compressed = huffman.compress(lipsum_string)
    decompressed = benchmark(huffman.decompress, compressed)
