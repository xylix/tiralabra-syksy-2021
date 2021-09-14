# Toteutusdokumentti

    
Program structure:
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

Performance, compression and O-analysis comparison:

(Execution speeds are relative to writer's own machine, a 2019 macbook pro with 2,3 GHz intel i9 CPU cores.)

- LZW:
    TODO: present o-analysis
- Huffman:
    TODO: present o-analysis
    -

How the project implementation deviates from the "specification":
    - 

Benchmarked comparisons:

-  100 kilobytes of simple Lorem Ipsum (A very easy file to compress):
    - LZW:
        - Compressed 100625 bytes to 53392 bytes, ratio: 0.5306037267080745
        - Takes ~125 milliseconds
    - Huffman:
        - Compressed 100625 bytes to 54164 bytes, ratio: 0.5382757763975156
        - Takes ~105 milliseconds
- 2 Megabytes of various ASCII data (holmes.txt):
    - LZW:
        - Compressed 6488666 bytes to 5185045 bytes, ratio: 0.7990926023931575
        - takes ~2.2 seconds
    - Huffman:
        - Compressed 6488666 bytes to 3683682 bytes, ratio: 0.567710219635284
        - takes ~1.5 seconds






Deficiencies and improvement ideas for the project:
- 


Sources:
- LZW:
    - 
- Huffman:
    - 
- visualize_tree.py: Original version from https://stackoverflow.com/a/65865825

