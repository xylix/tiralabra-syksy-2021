from enum import Enum
from io import UnsupportedOperation
import logging
from pathlib import Path
import sys
from sys import getsizeof

import typer

from . import lzw
from . import huffman


SUPPORTED_ARCHIVES = [".lzw", ".huffman"]
FILETYPES_TO_ARCHIVE = [".txt"]


class Algorithm(Enum):
    lzw = "lzw"
    huffman = "huffman"


class Operation(Enum):
    archive = "archive"
    extract = "extract"
    auto = "auto"


# The type ignores for enum params are necessary because typer has problems with enum default values
def main(
    filename: str,
    operation: Operation = "auto",  # type: ignore
    debug: bool = False,
    write_to_file: bool = False,
    algo: Algorithm = "huffman",  # type: ignore
):
    """
    LZW modules entry point
    """
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    logging.debug(f"Argument List: {sys.argv}")
    logging.debug(f"locals: {locals()}")

    if algo == Algorithm.lzw:
        module = lzw
    elif algo == Algorithm.huffman:
        module = huffman
    else:
        raise TypeError("Invalid algorithm specified")

    if operation not in Operation:
        raise TypeError("Invalid operation")

    if operation == operation.archive and (
        ".lzw" in filename or ".huffman" in filename
    ):
        raise UnsupportedOperation("Do not archive already archived files")

    def compress(input_data: bytes):
        output = module.compress(input_data)
        outf_name = f"{filename}.{algo.value}"
        return output, outf_name

    def decompress(input_data: bytes):
        output = module.decompress(input_data)
        outf_name = f"{filename}.out"
        return output, outf_name

    infile = Path(filename)

    with open(infile, "rb") as file:
        input_data = file.read()
    if operation == operation.archive:
        assert infile.suffix in FILETYPES_TO_ARCHIVE
        output, outf_name = compress(input_data)
    elif operation == operation.extract:
        assert infile.suffix in SUPPORTED_ARCHIVES
        output, outf_name = decompress(input_data)
    elif operation == operation.auto:
        logging.debug(f"Suffix: `{infile.suffix}`")

        if infile.suffix == ".lzw":
            module = lzw
        elif infile.suffix == ".huffman":
            module = huffman
        output: bytes
        if infile.suffix in SUPPORTED_ARCHIVES:
            output, outf_name = decompress(input_data)
        # TODO: add more supported input types
        elif infile.suffix in FILETYPES_TO_ARCHIVE:
            output, outf_name = compress(input_data)
        else:
            raise ValueError(
                f"Cannot figure out automatic operation type from {filename}"
            )

        # TODO: figure out the operation from filename
    else:
        raise UnsupportedOperation()

    if write_to_file:
        # TODO: figure out a more efficient storage format for the compressed output
        # maybe check https://docs.python.org/3/library/codecs.html
        with open(outf_name, "wb") as outf:
            # outf.write(bytes(output)
            outf.write(output)
    if len(output) < 16000:
        logging.debug(f"Created output: `{output}`")
    print(
        f"Compressed {len(input_data)} bytes to {len(output)} bytes, ratio: { len(output) / len(input_data) }"
    )


if __name__ == "__main__":
    typer.run(main)
