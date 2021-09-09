# Pseudocode examples from https://riptutorial.com/algorithm/example/23995/huffman-coding


def compress():
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
    pass


def decompress():
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
    pass


def main():
    print("hello world")


if __name__ == "__main__":
    main()
