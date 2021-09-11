from enum import Enum
from io import UnsupportedOperation
import logging
from pathlib import Path
import pickle
from typing import Optional

import typer

from . import lzw
from . import huffman


class Algorithm(Enum):
    lzw = "lzw"
    huffman = "huffman"


class Operation(Enum):
    archive = "archive"
    extract = "extract"
    auto = "auto"


def main(
    filename: str,
    operation: Operation = Operation.auto,
    debug: bool = True,
    write_to_file: bool = False,
    compression_algorithm: Algorithm = Algorithm.huffman,
):
    """
    LZW modules entry point
    """

    if compression_algorithm == Algorithm.lzw:
        module = lzw
    elif compression_algorithm == Algorithm.huffman:
        module = huffman
    else:
        raise TypeError("Invalid algorithm specified")

    if operation not in Operation:
        raise TypeError("Invalid operation")

    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)
    # logging.debug(f"Argument List: {sys.argv}")

    if operation == operation.archive and (".lzw" in filename or ".huff" in filename):
        raise UnsupportedOperation("Do not archive already archived files")

    def compress():
        with open(filename, "r", encoding="UTF-8") as file:
            output = module.compress(file.read())
            outf_name = f"{filename}.{compression_algorithm.value}"
        return output, outf_name

    def decompress():
        with open(filename, "rb") as file:
            output = module.decompress(pickle.load(file))
            outf_name = f"{filename}.out"
        return output, outf_name

    if operation.archive:
        output, outf_name = compress()
    elif operation.extract:
        output, outf_name = decompress()
    elif operation.auto:
        infile = Path(filename)
        if infile.suffix in [".lzw", ".huffman"]:
            pass

        # TODO: figure out the operation from filename
    else:
        raise UnsupportedOperation()

    if write_to_file:
        # TODO: figure out a more efficient storage format for the compressed output
        # maybe check https://docs.python.org/3/library/codecs.html
        with open(outf_name, "wb") as outf:
            pickle.dump(output, outf)
    logging.debug(f"Created output: `{output}`")


if __name__ == "__main__":
    typer.run(main)
