# Lzhuff

Kerkko Pelttari's algorithm project course work in fall 2021.

## Quickstart

Setup: create virtualenv (or don't) and run `pip install -r dev-requirements.txt`

Command line help: `python -m src.main --help`

NOTE: currently only ASCII .txt file compression is supported. Non ASCII files may fail with weird errors and non-txt files will fail with `UnsupportedOperation`.

Compress `filename` with LZW : `python -m src.main filename --algorithm lzw --write-to-file`
Compress `filename` with Huffman coding: `python -m src.main filename --algorithm huffman --write-to-file`

Extract `filename` (that has either .lzw or .huffman extension, algorithm is autodetectd) : `python -m src.main filename --write-to-file`



## Development

Run tests: `make test` 
Run performance tests: `make test-with-benchmarks`
Run simple benchmarks: `make simple-benchmarks`

### Profiling

Run with `python -m cProfile -o profile.out -s cumtime -m src.main` to profile


## Course documents
* [Definition document / määrittelydokumentti ](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/maarittely.md)
* [User guide  / käyttöohje](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/kayttoohje.md)
* [Testing document / testaus dokumentti](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/testaus.md)
	* [Test coverage history](https://github.com/xylix/tiralabra-syksy-2021/tree/main/dokumentit/coverage_history)
* [Implementation document / toteutusdokumentti](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/kayttoohje.md)
* [Weekly reports / Viikkoraportit](https://github.com/xylix/tiralabra-syksy-2021/tree/main/dokumentit/viikkoraportit)
	* [Week report 1](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/viikkoraportit/1.md)
	* [Week report 2](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/viikkoraportit/2.md)
	* [Week report 3](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/viikkoraportit/3.md)
	* [Week report 4](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/viikkoraportit/4.md)



