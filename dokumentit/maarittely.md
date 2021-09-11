# Definition document

## Programming language:

Planning to use primarily Python.

I can peer review projects in Python, Javascript (/ Typescript), Rust, Java, Kotlin, and possibly Haskell (no promises if the code is complicated)


## Planned algorithms and data structures to use in the program:

Standard library's dictionary for the LZW dict. Possible something improved later (an ordered Hash set?).

For the Huffman coding binary tree creation heapq (a good priority queue implementation) from the Python standard library should be useful.

Some improved string / constant length string operation data type could be useful. Might need to implement something by hand. (Or the compression data should be handled as binary instad of strings when optimizing.)

## The problem to solve

Program and compare implementations of LZW and Huffman coding. They are both popular algorithms for lossless compression. If comparing is too simple, make use of the algorithms to implement a variant of Deflate or such algorithm that uses both building blocks.


##  Program inputs

* Both compression implementations will take in a file path and as output write either compressed or decompressed files based on the input type.


## Time- and space complexity targets (including O-analysis)

The compression % targets depend on the data set. The goal is to match some comparable implementation's compression % and have compatible input and output formats. The specific files for benchmarking will be decided when the performance benchmarking is implemented, so around week 5.

* Huffman %
  * File 1, 12 paragraphs of lorem ipsum. Target compression % still unclear.
  * File 2, still to decide.

* LZW
  * File 1, 12 paragraphs of lorem ipsum. Target compression % still unclear.
  * File 2, still to decide.

Both algorithms are O(n) in their complexity, the use of hash-based data structures and necessity of only a single pass over the input data means that the execution time scales linearly.
  * However when adding un-optimized compression or decompression using the generated Huffman encoding bin tree that is `n log n` since the binary tree needs to be traversed for every symbol encoded. (Easy to optimize this to `O(n)` for the compression, harder to optimize for the decompression.)


## Sources
* LZ
  * https://en.wikipedia.org/wiki/LZ77_and_LZ78#LZ78
  * LZW https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch
  * LZW pseudocode: https://www2.cs.duke.edu/csed/curious/compression/lzw.html

* Huffman coding
  * https://en.wikipedia.org/wiki/Huffman_coding
  * Pseudocode: https://riptutorial.com/algorithm/example/23995/huffman-coding
  * Compression efficiency target https://en.wikipedia.org/wiki/Arithmetic_coding#Huffman_coding

## study program:
Bachelor's degree in computer science

## Language:
English (Can also peer review projects in finnish)

