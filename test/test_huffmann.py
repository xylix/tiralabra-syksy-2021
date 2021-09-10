from src import huffmann
from src.huffmann import Node, HuffmannResult


TEST_DATA = {
    "FIRST_SIMPLE_TEST_STRING": HuffmannResult(
        encoded="001110100011110111111010110000101100001000001101111000001111110101111001111100011000011",
        dictionary={
            "E": "0000",
            "M": "00010",
            "G": "00011",
            "L": "0010",
            "N": "00110",
            "F": "001110",
            "R": "001111",
            "S": "01",
            "I": "10",
            "P": "1100",
            "_": "1101",
            "T": "111",
        },
        bintree=Node(
            freq=24,
            symbol=None,
            left=Node(
                freq=13,
                symbol=None,
                left=Node(
                    freq=9,
                    symbol=None,
                    left=Node(
                        freq=4,
                        symbol=None,
                        left=Node(freq=2, symbol="E", left=None, right=None),
                        right=Node(
                            freq=2,
                            symbol=None,
                            left=Node(freq=1, symbol="M", left=None, right=None),
                            right=Node(freq=1, symbol="G", left=None, right=None),
                        ),
                    ),
                    right=Node(
                        freq=5,
                        symbol=None,
                        left=Node(freq=1, symbol="L", left=None, right=None),
                        right=Node(
                            freq=4,
                            symbol=None,
                            left=Node(freq=1, symbol="N", left=None, right=None),
                            right=Node(
                                freq=3,
                                symbol=None,
                                left=Node(freq=1, symbol="F", left=None, right=None),
                                right=Node(freq=2, symbol="R", left=None, right=None),
                            ),
                        ),
                    ),
                ),
                right=Node(freq=4, symbol="S", left=None, right=None),
            ),
            right=Node(
                freq=11,
                symbol=None,
                left=Node(freq=3, symbol="I", left=None, right=None),
                right=Node(
                    freq=8,
                    symbol=None,
                    left=Node(
                        freq=4,
                        symbol=None,
                        left=Node(freq=1, symbol="P", left=None, right=None),
                        right=Node(freq=3, symbol="_", left=None, right=None),
                    ),
                    right=Node(freq=4, symbol="T", left=None, right=None),
                ),
            ),
        ),
    )
}
TEST_LIPSUMFILE = "test_lipsum_10_paragraphs.txt"


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


def test_main():
    huffmann.main()
