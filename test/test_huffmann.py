from src import huffmann
from src.huffmann import Node


TEST_DATA = {
    "banana_bandana\n": (
        "binary encoding",
        Node(
            freq=15,
            symbol="\nd_nab",
            left=Node(
                freq=13,
                symbol="\nd_na",
                left=Node(
                    freq=7,
                    symbol="\nd_n",
                    left=Node(
                        freq=3,
                        symbol="\nd_",
                        left=Node(
                            freq=2,
                            symbol="\nd",
                            left=Node(freq=1, symbol="\n", left=None, right=None),
                            right=Node(freq=1, symbol="d", left=None, right=None),
                        ),
                        right=Node(freq=1, symbol="_", left=None, right=None),
                    ),
                    right=Node(freq=4, symbol="n", left=None, right=None),
                ),
                right=Node(freq=6, symbol="a", left=None, right=None),
            ),
            right=Node(freq=2, symbol="b", left=None, right=None),
        ),
    )
}
TEST_LIPSUMFILE = "test_lipsum_10_paragraphs.txt"


def test_preprocess():
    for cleartext, encoded in TEST_DATA.items():
        out = huffmann.preprocess(cleartext)
        assert out


def test_compress():
    for cleartext, encoded in TEST_DATA.items():
        out = huffmann.compress(cleartext)
        assert out == encoded


def test_decompress():
    for cleartext, (encoded, tree) in TEST_DATA.items():
        out = huffmann.decompress(tree, encoded)
        assert out == cleartext


def test_main():
    huffmann.main()
