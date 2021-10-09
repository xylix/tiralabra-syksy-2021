# Testing document

## Week 5 test coverage:
Name                          Stmts   Miss  Cover
-------------------------------------------------
src/__init__.py                   0      0   100%
src/huffman.py                   76      0   100%
src/lzw.py                       57      2    96%
src/main.py                      75      8    89%
src/utils/__init__.py             0      0   100%
src/utils/visualize_tree.py       1      1     0%
-------------------------------------------------
TOTAL                           209     11    95%

## Test explanations

All the main functionality of the current program is tested. (The compress and decompress methods of the LZW and Huffman modules and the main methods of both.) The tests were used as part of doing test-driven-development for the program, and especially for developing the Huffman part they often proved useful.

* As part of the debug logging of the program, it logs intermediate results and data types and I manually ensured that for example the Huffman tree looks as expected. However since other programs implementing Huffman output it in binary in a variety of ways it is hard to automatically test for the correctness of the encoding tree.

The current test data is a couple small strings and 12 paragraphs of lorem ipsum. Something even larger will be added as part of adding the benchmarking tests during the following weeks. Both algorithms are tested with same plaintext inputs but their intermediary data formats differ so their compressed results can't be validated against each other.

Tests can be run after installing the dependencies (create a virtual environment and run `pip install -r dev-requirements.txt`) `make test` or an `python -m pytest` in environments without make.



## Performance testing

Check [implementation document](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/toteutus.md)

