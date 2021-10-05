import pickle
from collections import Counter

from src import huffman
from src.huffman import HuffmanResult

# fmt: off
TEST_DATA = {
    b"FIRST_SIMPLE_TEST_STRING": HuffmanResult(encoded=3115303770153516478818454, freq_dict={70: 1, 73: 3, 82: 2, 83: 4, 84: 4, 95: 3, 77: 1, 80: 1, 76: 1, 69: 2, 78: 1, 71: 1})
}
# fmt: on


def test_freq_dict():
    for cleartext, expected_output in TEST_DATA.items():
        out = Counter(cleartext)
        assert out == expected_output.freq_dict


def test_compress():
    for cleartext, expected_output in TEST_DATA.items():
        out = huffman.compress(cleartext)
        assert pickle.loads(out) == expected_output


def test_decompress():
    for cleartext, expected_output in TEST_DATA.items():
        out = huffman.decompress(pickle.dumps(expected_output))
        assert out == cleartext


def test_longer_input_file(lipsum):
    compressed = huffman.compress(lipsum)
    decompressed = huffman.decompress(compressed)
    assert lipsum == decompressed
