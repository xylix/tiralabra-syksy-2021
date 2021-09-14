#!/bin/sh

echo "## LZW 100kb_lipsum.txt"
time python -m src.main --algo huffman test/resources/100kb_lipsum.txt --write-to-file
time python -m src.main --algo huffman test/resources/100kb_lipsum.txt.huffman --write-to-file

echo "## Huffman 100kb_lipsum.txt"
time python -m src.main --algo lzw test/resources/100kb_lipsum.txt --write-to-file
time python -m src.main --algo lzw test/resources/100kb_lipsum.txt.lzw --write-to-file

echo "## LZW 6_2mb_lipsum.txt"
time python -m src.main --algo huffman test/resources/6_2mb_lipsum.txt --write-to-file
time python -m src.main --algo huffman test/resources/6_2mb_lipsum.txt.huffman --write-to-file

echo "## Huffman 6_2mb_lipsum.txt"
time python -m src.main --algo lzw test/resources/6_2mb_lipsum.txt --write-to-file
time python -m src.main --algo lzw test/resources/6_2mb_lipsum.txt.lzw --write-to-file

echo "## LZW holmes.txt"
time python -m src.main --algo huffman test/resources/holmes.txt --write-to-file
time python -m src.main --algo huffman test/resources/holmes.txt.huffman --write-to-file

echo "## Huffman holmes.txt"
time python -m src.main --algo lzw test/resources/holmes.txt --write-to-file
time python -m src.main --algo lzw test/resources/holmes.txt.lzw --write-to-file

echo "cleanup"

rm test/resources/100kb_lipsum.txt.huffman \
test/resources/100kb_lipsum.txt.huffman.out \
test/resources/100kb_lipsum.txt.lzw \
test/resources/100kb_lipsum.txt.lzw.out \
test/resources/6_2mb_lipsum.txt.huffman \
test/resources/6_2mb_lipsum.txt.huffman.out \
test/resources/6_2mb_lipsum.txt.lzw \
test/resources/6_2mb_lipsum.txt.lzw.out \
test/resources/holmes.txt.huffman.out
