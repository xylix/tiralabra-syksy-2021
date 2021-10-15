# Usage instructions

## Usage

Setup: create virtualenv (or don't) and run `pip install -r dev-requirements.txt`


Command line help: `python -m src.main --help`


Compress `filename` with LZW (Should be an ASCII or UTF-8): `python -m src.main filename --algorithm lzw --write-to-file`
Compress `filename` with Huffman coding: `python -m src.main filename --algorithm huffman --write-to-file`


Extract `filename` (that has either .lzw or .huffman extension, algorithm is autodetectd) : `python -m src.main filename --write-to-file`

## Tests

Run tests: `make test` 
Run performance tests: `make test-with-benchmarks`
