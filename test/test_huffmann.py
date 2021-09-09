from src import huffmann


TEST_DATA = {"banana_bandana\n": "hufftree will be here"}
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
    for cleartext, encoded in TEST_DATA.items():
        out = huffmann.decompress(encoded)
        assert out == cleartext


def test_main():
    huffmann.main()
