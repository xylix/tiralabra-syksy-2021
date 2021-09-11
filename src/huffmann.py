from dataclasses import dataclass
from heapq import heappop, heappush
import logging
from typing import Dict, Iterable, List, Optional, Tuple

from .utils.visualize_tree import print_tree

# Pseudocode examples from https://riptutorial.com/algorithm/example/23995/huffman-coding


def preprocess(data: str) -> Dict[str, int]:
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
class HuffmannResult:
    """Represents"""

    encoded: str
    dictionary: Dict[str, str]
    bintree: Node


def transform_bintree(root) -> Dict[str, str]:
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


def compress(data: str) -> HuffmannResult:
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
    output = ""
    for char in data:
        encoded_char: str = encoding_dict[char]
        output += encoded_char
    return HuffmannResult(str(output), encoding_dict, q[0])


def decompress(input_data: HuffmannResult) -> str:
    # pylint: disable=invalid-name
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
    # Can't use handy dict for decompression because the tree also encodes the information of at what point which symbol terminates
    S = input_data.encoded
    root = input_data.bintree
    output = ""
    n = len(S)
    print(n)
    # While instead of for because it's easier to skip entries with this than with Python's for
    i = 0
    while i < n:
        current = root
        # We can use and here since the tree is balanced
        while current.left and current.right:
            if S[i] == "0":
                current = current.left
            else:
                current = current.right
            i = i + 1
        # The terminal nodes should always have a symbol
        assert current.symbol
        output += current.symbol
    return output


def main():
    """
    Huffmann modules entry point
    """
    debug = True
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    compress_output = compress("FIRST_SIMPLE_TEST_STRING")
    logging.debug("bintree: \n" + "\n".join(print_tree(compress_output.bintree)))
    logging.debug(f"encoded: {repr(compress_output.encoded)}")
    logging.debug(f"dict: {repr(compress_output.dictionary)}")

    # logging.debug(repr(compress_output))


if __name__ == "__main__":
    main()
