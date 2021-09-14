# Toteutusdokumentti

    
## Program structure:
- src/ contains the program code
    - main.py is the main CLI and entry point for the program.
    - lzw.py is the implementation of the LZW compression algorithm
    - huffman.py is the implementation of the Huffman compression algorithm
    - utils/ contains a single utility file:
        - visualize_tree.py is a helper for printing tree data structures visually on the command line (found on stackoverflow)
            - Not in use currently, it prints quite large amount of rows and columns. But useful for figuring out what Huffman compression trees look like.

- test/ contains the test code
    - test_lzw.py test_huffman.py and test_main.py contain unit tests and some slower benchmark tests for the corresponding modules
        - run normal tests with `make test`, slower tests with `make test-with-benchmarks`
    - test/resources contains the test input files

## Performance, compression and O-analysis comparison:

- LZW:
    TODO: present o-analysis
- Huffman:
    TODO: present o-analysis
    -

How the project implementation deviates from the "specification":
    - Data is read as chars, not bytes. It is written with significant overhead by using python's pickle module, and currently (as of week 4) this overhead affects 


Execution times are relative to writer's own machine, a 2019 macbook pro with 2,3 GHz intel i9 CPU cores. Tests were run a couple of times, and the recorded results were chosen from the more average ones. Deviation analysis was deemed out of scope for this report.

Compression ratios written as xy% of data remaining after the compression operation.

Benchmarked comparisons:

### 100 kilobytes of simple Lorem Ipsum (A very easy file to compress)
100kb_lipsum.txt
| Algorithm     | Compression time | Decompression time | Compression ratio |
| ------------- | ---------------- | ------------------ | ----------------- |
| LZW           | 90 milliseconds  | 145 milliseconds   | 54%               |
| Huffman       | 98 milliseconds  | 80 milliseconds    | 53%               |


### 6.2 Megabytes of simple Lorem Ipsum (A very easy but larger file to compress) 
6_2mb_lipsum.txt

| Algorithm     | Compression time  | Decompression time |  Compression ratio |
| ------------- | ----------------  | ------------------ | -----------------  |
| LZW           | 1.43 seconds      | 5.38 seconds       | % 54%              |
| Huffman       | 2.06 seconds      | 0.55 seconds       | % 44%              |

    
### 6.2 Megabytes of varying ASCII text 
holmes.txt
| Algorithm     | Compression time | Decompression time | Compression ratio |
| ------------- | ---------------- | ------------------ | ----------------- |
| LZW           | 1.58 seconds     | 5.79 seconds       | 57%               |
| Huffman       | 1.09 seconds     | 1.03 seconds       | 79%               |


As we can notice, LZW decompression time grows as a function of the input size, whereas with Huffman the algorithm time grows as a function of the compression ratio and file size. Further analysis will be done.

Both algorithms time complexities should also be affected by the amount of symbols in the input data. This will also be mapped in a future analysis.


## Deficiencies and improvement ideas for the project:
- 


## Sources:
- LZW:
    - 
- Huffman:
    - 
- visualize_tree.py: Original version from https://stackoverflow.com/a/65865825

