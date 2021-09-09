from src import lzw


# Once the algorithm works we will be able to use same test data, just in reverse

TEST_COMPRESS_DATA = {"banana_bandana": "98,97,110,129,97,95,128,110,100,131,"}


def test_compress():
    for inp, outp in TEST_COMPRESS_DATA.items():
        out = lzw.compress(inp)
        assert out == outp


TEST_DECOMPRESS_DATA = {"98,97,110,129,97,95,128,110,100,131": "ban98aa_98bnd1109"}


def test_decompress():
    for inp, outp in TEST_DECOMPRESS_DATA.items():
        out = lzw.decompress(inp)
        assert out == outp


# def test_main():
#    lzw.main()
