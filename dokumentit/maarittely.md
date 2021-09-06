# Definition document

## Programming language:

Planning to use primarily Python, and if allowed Rust (or C or Java) for performance critical parts.

I can peer review projects in Python, Javascript (/ Typescript), Rust, Java, Kotlin, and possibly Haskell (no promises if the code is complicated)


## Planned algorithms and data structures to use in the program:

[Zstandard](https://en.wikipedia.org/wiki/Zstandard) is a quite complicated algorithm (see references in sources section). 

The goal for the project is to first read through and mostly understand the zstandard specification, and then re-implement meaningful parts of zstandard in Python. (Re-implementing the entire project would be too large in scope, but I also can not yet say which parts are the most important ones. It will be specified when the information is found.)

Other algorithms that are highly relevant in zstandard's implementation include FSE (Finite State Entropy) 


## The problem to solve

Create a partially pure-python implementation of the decoding process of zstandard, that relies on the existing c implementation and it's python bindings where needed. The plan is _not_ to just create alternative python bindings for zstandard, but instead implement critical parts of decompressing zstandard in python and or even pseudocode for ease of learning. As of writing this document the only Zstandard implementations (that were not just bindings) are in C, Golang and Rust.

In making it possible to pick a scope like the above, the scope of the resulting python program will be planned quite a lot smaller than real Zstandards. Just implementing single file non-streaming zstandard decompression coule be sufficient. If the decompression proves too easy compression will also be implemented.

The program will be tested by comparing file checksums after a complete decompression to a decompression of the same file with the reference implementation.

Zstandard being a compression algorithm, for the purposes of this course project the slowness of Python should not be a problem. However if the performance is a problem it is an option to implement performance critical parts in Rust or C or Java.
 


##  Program inputs

* The program takes in a file descriptor / path whose size can fit in RAM, and compresses it according to Zstandard.
* If there is extra time, the configuration option that Zstandard offers of adjusting the execution speed / compression ratio could be offered.


##  Tavoitteena olevat aika- ja tilavaativuudet (m.m. O-analyysit)

* The program aims to match the compression performance of the Zstandard reference implementation for the parts the program implements.
* There are no specific time complexity goals, but analysis can be done for the parts of the program that behave slower than the reference implemntation.


## Sources
* Original publication: https://engineering.fb.com/2016/08/31/core-data/smaller-and-faster-data-compression-with-zstandard/
* The official reference implementation https://github.com/facebook/zstd
* The reference RFC https://datatracker.ietf.org/doc/html/rfc8478
  * The subsection focused on the algorithm https://datatracker.ietf.org/doc/html/rfc8478#section-3
  * FSE - Finite State Entropy https://github.com/Cyan4973/FiniteStateEntropy/


## study program:
Bachelor's degree in computer science

## Language:
English (Can also peer review projects in finnish)

