import logging
from typing import Dict, Optional, List, Iterable, Tuple
from heapq import heappush, heappop
from dataclasses import dataclass

from .utils.visualize_tree import print_tree

# Pseudocode examples from https://riptutorial.com/algorithm/example/23995/huffman-coding


def preprocess(data: str) -> Dict[str, int]:
    chardict = {}
    for c in data:
        if c in chardict:
            chardict[c] += 1
        else:
            chardict[c] = 1
    return chardict


@dataclass
class Node:
    freq: float
    symbol: Optional[str]
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __lt__(self, other):
        self.freq < other.freq


@dataclass
class HuffmannResult:
    encoded: str
    dictionary: Dict[str, str]
    bintree: Node


def transform_bintree(root) -> Dict[str, str]:
    initial_binary = ""
    output = {}

    def helper(curr_binary, currnode) -> Iterable[Tuple[str, str]]:
        yield currnode.symbol, curr_binary
        if currnode.left:
            yield from helper(curr_binary + "0", currnode.left)

        if currnode.right:
            yield from helper(curr_binary + "1", currnode.right)

    for outval in helper(initial_binary, root):
        output[outval[0]] = outval[1]
    del output[None]

    return output


def compress(data: str) -> HuffmannResult:
    """
    Procedure Huffman(C):     // C is the set of n characters and related information
    n = C.size
    Q = priority_queue()
    for i = 1 to n
        n = node(C[i])
        Q.push(n)
    end for
    while Q.size() is not equal to 1
        Z = new node()
        Z.left = x = Q.pop
        Z.right = y = Q.pop
        Z.frequency = x.frequency + y.frequency
        Q.push(Z)
    end while
    Return Q
    """
    c = preprocess(data)
    q: List[Node] = []
    for symbol, freq in c.items():
        node = Node(freq, symbol)
        heappush(q, node)
    # FIXME: it seems there is some problem with the tree's weighting. It leans heavily to the left
    while len(q) > 1:
        left = heappop(q)
        right = heappop(q)
        freq = left.freq + right.freq
        z = Node(freq, None, left, right)
        heappush(q, z)

    logging.debug(q[0])
    # Transform the binary tree to a dictionary
    encoding_dict = transform_bintree(q[0])
    logging.debug(encoding_dict)

    # Use the created binary tree to encode the data. Could not find a pseudo code for this, might need to create one.
    output = ""
    for char in data:
        encoded_char: str = encoding_dict[char]
        output += encoded_char
    return HuffmannResult(str(output), encoding_dict, q[0])


def decompress(input: HuffmannResult):
    """
    Procedure HuffmanDecompression(root, S):   // root represents the root of Huffman Tree
    n := S.length                              // S refers to bit-stream to be decompressed
    for i := 1 to n
        current = root
        while current.left != NULL and current.right != NULL
            if S[i] is equal to '0'
                current := current.left
            else
                current := current.right
            endif
            i := i+1
        endwhile
        print current.symbol
    endfor
    """
    data = input.encoded
    output = ""
    n = len(data)
    for i in range(n):
        current = input.bintree
        while current.left and current.right:
            if data[i] == 0:
                current = current.left
            else:
                current = current.right
            i += 1
        output += current.symbol or ""
    return output


def main():
    debug = True
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    compress_output = compress("FIRST_SIMPLE_TEST_STRING")
    print_tree(compress_output.bintree)
    print(repr(compress_output))


if __name__ == "__main__":
    main()
