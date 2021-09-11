from pathlib import Path

import pytest

from src import huffmann
from src.huffmann import HuffmannResult, Node

# fmt: off
TEST_DATA = {
    "FIRST_SIMPLE_TEST_STRING": HuffmannResult(encoded='1010010011101100001111010010101101110101111101100111111000011110001110100010010110', dictionary={'T': '00', 'N': '0100', 'L': '0101', '_': '011', 'I': '100', 'F': '10100', 'M': '10101', 'G': '10110', 'P': '10111', 'S': '110', 'R': '1110', 'E': '1111'}, bintree=Node(freq=24, symbol=None, left=Node(freq=9, symbol=None, left=Node(freq=4, symbol='T', left=None, right=None), right=Node(freq=5, symbol=None, left=Node(freq=2, symbol=None, left=Node(freq=1, symbol='N', left=None, right=None), right=Node(freq=1, symbol='L', left=None, right=None)), right=Node(freq=3, symbol='_', left=None, right=None))), right=Node(freq=15, symbol=None, left=Node(freq=7, symbol=None, left=Node(freq=3, symbol='I', left=None, right=None), right=Node(freq=4, symbol=None, left=Node(freq=2, symbol=None, left=Node(freq=1, symbol='F', left=None, right=None), right=Node(freq=1, symbol='M', left=None, right=None)), right=Node(freq=2, symbol=None, left=Node(freq=1, symbol='G', left=None, right=None), right=Node(freq=1, symbol='P', left=None, right=None)))), right=Node(freq=8, symbol=None, left=Node(freq=4, symbol='S', left=None, right=None), right=Node(freq=4, symbol=None, left=Node(freq=2, symbol='R', left=None, right=None), right=Node(freq=2, symbol='E', left=None, right=None))))))
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
        out = huffmann.preprocess(cleartext)
        assert out


def test_compress():
    for cleartext, expected_output in TEST_DATA.items():
        out = huffmann.compress(cleartext)
        assert out == expected_output


def test_decompress():
    for cleartext, expected_output in TEST_DATA.items():
        out = huffmann.decompress(expected_output)
        assert out == cleartext


def test_longer_input_file():
    with open(Path(__file__).parent / TEST_LIPSUMFILE) as f:
        data = f.read()
    compressed = huffmann.compress(data)
    decompressed = huffmann.decompress(compressed)
    assert data == decompressed


@pytest.mark.slow
def test_benchmark_huffmann_compression(lipsum_string, benchmark):
    compressed = benchmark(huffmann.compress, lipsum_string)


@pytest.mark.slow
def test_benchmark_huffmann_decompression(lipsum_string, benchmark):
    compressed = huffmann.compress(lipsum_string)
    decompressed = benchmark(huffmann.decompress, compressed)
