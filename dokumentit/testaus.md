# Testing document

## Week 3 test coverage:
Name                          Stmts   Miss  Cover
-------------------------------------------------
src/__init__.py                   0      0   100%
src/huffman.py                  89      2    98%
src/lzw.py                       63      0   100%
src/utils/__init__.py             0      0   100%
src/utils/visualize_tree.py      44     14    68%
-------------------------------------------------
TOTAL                           196     16    92%


All the main functionality of the current program is tested. (The compress and decompress methods of the LZW and Huffman modules and the main methods of both.) The tests were used as part of doing test-driven-development for the program, and especially for developing the Huffman part they often proved useful.

* As part of the debug logging of the program, it logs intermediate results and data types and I manually ensured that for example the Huffman tree looks as expected. However since other programs implementing Huffman output it in binary in a variety of ways it is hard to automatically test for the correctness of the encoding tree.

The current test data is a couple small strings and 12 paragraphs of lorem ipsum. Something even larger will be added as part of adding the benchmarking tests during the following weeks. Both algorithms are tested with same plaintext inputs but their intermediary data formats differ so their compressed results can't be validated against each other.

Tests can be run after installing the dependencies (create a virtual environment and run `pip install -r dev-requirements.txt`) `make test` or an `python -m pytest` in environments without make.


## Week 4 test coverage:


## Performance testing

### First results at bccf6cb7a8a11c1c24ca76ddd7c0d5d8eb76774d, just after adding performance tests
------------------------------------------------------------------------------------------- benchmark: 4 tests -------------------------------------------------------------------------------------------
Name (time in ms)                             Min                Max               Mean            StdDev             Median               IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_benchmark_huffman_compression        1.1669 (1.0)       2.6013 (1.0)       1.2773 (1.0)      0.1836 (1.0)       1.2054 (1.0)      0.1093 (1.0)         76;77  782.8813 (1.0)         788           1
test_benchmark_huffman_decompression      4.1947 (3.59)      7.2604 (2.79)      4.6994 (3.68)     0.4774 (2.60)      4.5077 (3.74)     0.4550 (4.16)        22;12  212.7930 (0.27)        225           1
test_benchmark_lzw_compression            12.7502 (10.93)    17.2397 (6.63)     13.4128 (10.50)    0.8559 (4.66)     13.0891 (10.86)    0.5870 (5.37)          6;6
   74.5554 (0.10)         62           1
test_benchmark_lzw_decompression          53.5811 (45.92)    57.2172 (22.00)    54.6676 (42.80)    1.1089 (6.04)     54.2377 (45.00)    1.3358 (12.22)         3;1   18.2924 (0.02)         19           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
======================================================================= 14 passed in 5.27s =======================================================================
