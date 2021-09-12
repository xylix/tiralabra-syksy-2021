from dataclasses import dataclass
from heapq import heappop, heappush
import logging
from typing import Dict, Iterable, List, Optional, Tuple

from src.utils.binary import number_to_binary

from .utils.visualize_tree import print_tree

# Pseudocode examples from https://riptutorial.com/algorithm/example/23995/huffman-coding


def preprocess(data: bytes) -> Dict[str, int]:
    """Generate character frequency dictionary from input_data data"""
    chardict = {}
    for char in data:
        if char in chardict:
            chardict[char] += 1
        else:
            chardict[char] = 1
    return chardict


@dataclass
class Node:
    """
    Single node of a nonstandard binary tree where every node has a `freq` field.
    """

    freq: float
    symbol: Optional[str]
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __lt__(self, other):
        return self.freq < other.freq


@dataclass
class HuffmanResult:
    """Represents"""

    encoded: bytes
    bintree: Node


def transform_bintree(root) -> Dict[int, str]:
    """
    Transforms the binary tree starting from `root` into a dictionary where dict[symbol]
    contains the path to the node encoded as a binary string.

    Example: node located left left right from `root` gets value "001" in the resulting dict
    """
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


def compress(data: bytes) -> HuffmanResult:
    # pylint: disable=invalid-name
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
    while len(q) > 1:
        left = heappop(q)
        right = heappop(q)
        freq = left.freq + right.freq
        z = Node(freq, None, left, right)
        heappush(q, z)

    # logging.debug(q[0])
    # Transform the binary tree to a dictionary
    encoding_dict = transform_bintree(q[0])
    logging.debug(encoding_dict)

    # Use the created binary tree to encode the data. Could not find a pseudo code for this, might need to create one.
    output: bytes = bytes()
    for char in data:
        encoded_char: str = encoding_dict[char]
        output += number_to_binary(int(encoded_char, 2))
    return HuffmanResult(output, q[0])


def decompress(input_data: HuffmanResult) -> str:
    # pylint: disable=invalid-name
    """
    Decompress a huffman encoded data, requires the encoded data and the huffman tree as input

    """
    logging.debug(input_data)
    # Can't use handy dict for decompression because the tree also encodes the information of at what point which symbol terminates
    S: bytes = input_data.encoded
    handy_dict = transform_bintree(input_data.bintree)
    dictionary = dict((v, k) for k, v in handy_dict.items())

    def translate(code: int) -> str:
        # There is probably a bit operator for this
        transformed_code = bin(code)[2:]
        logging.debug(transformed_code)

        return chr(dictionary[transformed_code])

    return "".join([translate(i) for i in S])
