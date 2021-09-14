from enum import Enum
from io import UnsupportedOperation
import logging
from pathlib import Path
import sys
from typing import Tuple

import typer

from . import lzw
from . import huffman


SUPPORTED_ARCHIVES = [".lzw", ".huffman"]
# TODO: add more supported input types, specifically UTF-8
FILETYPES_TO_ARCHIVE = [".txt"]


class Algorithm(Enum):
    "Supported encoding and decoding algorithms."
    LZW = "lzw"
    HUFFMAN = "huffman"


class Operation(Enum):
    """Supported operations."""

    ARCHIVE = "archive"
    EXTRACT = "extract"
    AUTO = "auto"


def _determine_module_from_algo(algo: Algorithm):
    """ """
    if algo == Algorithm.LZW:
        return lzw
    elif algo == Algorithm.HUFFMAN:
        return huffman
    else:
        raise TypeError("Invalid algorithm specified")


def _determine_module_from_suffix(suffix: str):
    """Determine compression / decompression module to use from given suffix."""
    if suffix == ".lzw":
        return lzw
    elif suffix == ".huffman":
        return huffman
    else:
        return None


def _decompress(module, filename, input_data: bytes) -> Tuple[bytes, str]:
    output = module.decompress(input_data)
    outf_name = f"{filename}.out"

    print(
        f"Decompressed {len(input_data)} bytes to {len(output)} bytes, ratio: { len(output) / len(input_data) }"
    )
    return output, outf_name


def _compress(module, filename: str, original_suffix: str, input_data: bytes):
    output = module.compress(input_data)
    outf_name = f"{filename}.{original_suffix}"
    print(
        f"Compressed {len(input_data)} bytes to {len(output)} bytes, ratio: { len(output) / len(input_data) }"
    )

    return output, outf_name


def _auto_operate(
    module, infile: Path, input_data: bytes, filename: str
) -> Tuple[bytes, str]:
    logging.debug(f"Suffix: `{infile.suffix}`")

    # If we are using operation.AUTO we override from the parameter
    module = _determine_module_from_suffix(infile.suffix)

    if infile.suffix in SUPPORTED_ARCHIVES:
        return _decompress(module, filename, input_data)
    elif infile.suffix in FILETYPES_TO_ARCHIVE:
        return _compress(module, filename, infile.suffix, input_data)
    else:
        raise ValueError(f"Cannot figure out automatic operation type from {filename}")


def _validate_operation(operation: Operation, filename: str):
    if operation not in Operation:
        raise TypeError("Invalid operation")

    if operation == operation.ARCHIVE and (
        ".lzw" in filename or ".huffman" in filename
    ):
        raise UnsupportedOperation("Do not archive already archived files")


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

    module = _determine_module_from_algo(algo)

    _validate_operation(operation, filename)

    infile = Path(filename)
    with open(infile, "rb") as file:
        input_data = file.read()

    if operation == operation.ARCHIVE:
        assert infile.suffix in FILETYPES_TO_ARCHIVE
        output, outf_name = _compress(module, filename, infile.suffix, input_data)
    elif operation == operation.EXTRACT:
        assert infile.suffix in SUPPORTED_ARCHIVES
        output, outf_name = _decompress(module, filename, input_data)
    elif operation == operation.AUTO:
        output, outf_name = _auto_operate(module, infile, input_data, filename)

    if write_to_file:
        # TODO: figure out a more efficient storage format for the compressed output
        # maybe check https://docs.python.org/3/library/codecs.html
        with open(outf_name, "wb") as outf:
            outf.write(output)
    if len(output) < 16000:
        print(f"Created output: `{output}`")
    elif not write_to_file:
        print("Output quite long to print, please use --write-to-file")


if __name__ == "__main__":
    typer.run(main)
