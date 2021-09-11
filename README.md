# Lzhuff

Kerkko Pelttari's algorithm project course work in fall 2021.

## Quickstart

Setup: create virtualenv (or don't) and run `pip install -r dev-requirements.txt`

Command line help: `python -m src.main --help`

Compress `filename` with LZW : `python -m src.main filename --operation archive --algorithm lzw`
Compress `filename` with Huffman coding: `python -m src.main filename --operation archive --algorithm huffman`

Extract `filename` (that has either .lzw or .huffman extension) : `python -m src.main filename --operation extract `


Run tests: `make test` 
Run performance tests: `make test-with-benchmarks`


## Course documents
* [Definition document / määrittelydokumentti ](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/maarittely.md)
* [User guide  / käyttöohje](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/kayttoohje.md)
* [Testing document / testaus dokumentti](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/testaus.md)
	* [Test coverage history](https://github.com/xylix/tiralabra-syksy-2021/tree/main/dokumentit/coverage_history)
* [Implementation document / toteutusdokumentti](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/kayttoohje.md)
* [Weekly reports / Viikkoraportit](https://github.com/xylix/tiralabra-syksy-2021/tree/main/dokumentit/viikkoraportit)
	* [Week report 1](https://github.com/xylix/tiralabra-syksy-2021/blob/main/dokumentit/viikkoraportit/1.md)



