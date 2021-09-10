from typing import Dict, Optional
from heapq import heappush
from dataclasses import dataclass

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
    symbol: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

    def __lt__(self, other):
        self.freq < other.freq


def compress(data: str) -> str:
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
    q = []
    for symbol, freq in c.items():
        node = Node(freq, symbol)
        heappush(q, node)
    while len(q) > 1:
        left = q.pop()
        right = q.pop()
        freq = left.freq + right.freq
        z = Node(freq, left.symbol + right.symbol, left, right)
        heappush(q, z)

    # TODO: use the created tree to encode the data here

    return str(q)


def decompress(tree_root: Node, data: str):
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
    output = ""
    n = len(data)
    for i in range(n):
        current = tree_root
        while current.left and current.right:
            if data[i] == 0:
                current = current.left
            else:
                current = current.right
            i += 1
        output += current.symbol
    return output


def main():
    print(repr(compress("FIRST_SIMPLE_TEST_STRING")))


if __name__ == "__main__":
    main()
